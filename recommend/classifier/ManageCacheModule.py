import sys
from classifier.GetRecommendationModule import GetRecommendation
from LocalStorage.AccessLocalStorageModule import AccessLocalStorage
from Metadata.ManageMetaDataModule import ManageMetaData
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
from PyQt5 import QtWidgets

"""
predictedSong dict should contain list elements and in the list the order of elements should be:
Title
Artist
URI

Type: boolean -> 0 for local , 1 for online
"""


class ManageCache:

    def __init__(self, connectionName):
        self.connectionName = connectionName
        # self.db = QSqlDatabase.addDatabase('QSQLITE', self.connectionName)
        self.db=QSqlDatabase.database(self.connectionName)
        self.buildCache()
        self.query = QSqlQuery(self.db)
        self.recommendedSongDict = {}
    """
    Considering the documentation of the project we have an important function missing which builds the cache, so we are adding it here
    """

    def getConnectionName(self):
        return self.connectionName

    def setConnectionName(self, connectionName):
        self.connectionName = connectionName

    def buildCache(self):
        # print("building Cache Db")
        # self.db.setDatabaseName('PRCache.sqlite3')
        # self.db.setUserName('ProjectRecommend')
        # self.db.setPassword('elite1338')
        # self.db.setPort(1338)

        if not self.db.isOpen():
            print("could not open the Cache database")
            return False
        else:
            print("opened the Cache database successfully")

        query = QSqlQuery(self.db)
        # for now i am not sure what is the data that will be stored in the cache and so i keep on SID and Spath for now

        isQuerySuccessful = query.exec_("create table cache(SPath varchar(255), SPathRec varchar(255), Title varchar(255),Artist varchar(255))")
        # URI will be the songPath in case the song is in the local PC and will be url in case the song is online

        if isQuerySuccessful:
            print("table Cache successfully created")
            return False
        else:
            print("table cache could not be created")
            print("error:")
            print(query.lastError().text())
        return True

    def readCache(self, SPath):
        # SPath is the path of song for which we are reading Cached recommendation
        if self.db.isOpen():
            queryString = "SELECT SPath, SPathRec, Title, Artist FROM cache WHERE SPath=:SPath"
            self.query.prepare(queryString)
            self.query.bindValue(":SPath", SPath)
            record = self.query.exec_()
            if record:
                print("read successful ")
                a = 0
                while self.query.next():
                    print("executing times:")
                    print(a)
                    a = a+1
                    self.recommendedSongDict["SPath"] = self.query.value(0)
                    self.recommendedSongDict["SPathRec"] = self.query.value(1)
                    self.recommendedSongDict["Title"] = self.query.value(2)
                    self.recommendedSongDict["Artist"] = self.query.value(3)
            else:
                print("read unsuccessful")
                print("error")
                print(self.query.lastError().text())
        else:
            print("connection is not open")
            return False
        return self.recommendedSongDict

    def writeCache(self, recommendedSongsPathList, SPath):
        # recommendedSongsPathList is a list that contains path of all recommended Songs Path
        isQuerySuccessful = None
        if self.db.isOpen():
            # print("trying to write in DB")
            for item in recommendedSongsPathList:
                metadataDict = ManageMetaData.ReadMetaData(self, item)
                self.query.prepare("insert into cache(SPath, SPathRec, Title, Artist) values(:SPath, :SPathRec, :Title, :Artist)")
                self.query.bindValue(":SPath", SPath)
                self.query.bindValue(":SPathRec", item)
                self.query.bindValue(":Title", metadataDict.get("TIT2", "NULL"))
                self.query.bindValue(":Artist", metadataDict.get("TPE1", "NULL"))
                isQuerySuccessful = self.query.exec_()
            if isQuerySuccessful:
                print("insertion successful")
                # print("no of rows affected: " + str(self.query.numRowsAffected()))
            elif self.query.lastError().number() is 19:
                pass
                print("unique Construct failed")
                # print(self.query.lastError().number().text())
            else:
                self.buildMessageBox("Not Enough Data to recommend songs for this song, please update metadata or add more songs to collection")
                print("insertion not successful")
                # print("error:")
                print(self.query.lastError().number())
                return False
        else:
            print("connection could not be established")
            return False
        return True

    def invalidateCache(self):
        return False

    def dumpCache(self):
        self.db.database(self.connectionName, False)
        # just to close the connection I use False as the second parameter
        query = QSqlQuery(self.db)
        isDeleteSuccessful = query.exec_("drop table cache")

        if isDeleteSuccessful:
            print("the table has been deleted successfully")
        else:
            print("the table could not be deleted")
            print("error:")
            print(query.lastError().text())
        return True

    def deleteCache(self, SPath):
        if self.db.isOpen():
            self.query.prepare("delete from songs WHERE SPath=:SPath")
            self.query.bindValue(":SPath", SPath)
            isQuerySuccessful = self.query.exec_()
            if isQuerySuccessful:
                print("----------------------------------------------")
                print("deletion successful")
            else:
                print("----------------------------------------------")
                print("could not delete")
                print("error")
                print(self.query.lastError().text())
        else:
            print("could not establish a connection")
            return False
        return True

    def queryCache(self, SPath, manageLocalStorage):
        projectModel = QSqlQueryModel()
        if self.db.open():
            query = QSqlQuery(self.db)
            print("in queryCache")
            print(SPath)
            query.prepare("select SPathRec, Title, Artist from cache WHERE SPath=:SPath ")
            query.bindValue(":SPath", SPath)
            query.exec_()
            projectModel.setQuery(query)
            print("num of row returned queryCache:")
            print(query.numRowsAffected())
            # print("query row count")
            if projectModel.rowCount() == 0:
                print("get recommendation, nothing is in Cache for this song")
                recommendedSongsPathList = []
                getRecom = GetRecommendation(manageLocalStorage)
                relevantSongDict = getRecom.fetchRelevantSongOffline(SPath)
                if SPath:
                    recommendedSongsPathList = getRecom.predict(SPath, relevantSongDict)
                else:
                    print("problem with SongPath so can't call predict")
                # if playing song is also recommended then remove it
                if SPath in recommendedSongsPathList:
                    recommendedSongsPathList.remove(SPath)
                # for item in recommendedSongsPathList:
                    # print(item)
                # build cache
                if self.writeCache(recommendedSongsPathList, SPath):
                    print("re Querying ")
                    projectModel.clear()
                    requery = QSqlQuery(self.db)
                    requery.prepare("select SPathRec, Title, Artist from cache WHERE SPath=:SPath ")
                    requery.bindValue(":SPath", SPath)
                    requery.exec_()
                    projectModel.setQuery(requery)
                    print("row Count After re query ")
                    print(projectModel.rowCount())
        else:
            print("Query failed")
        return projectModel

    def buildMessageBox(self, message):
        messageBox = QtWidgets.QMessageBox()
        messageBox.setText(message)
        messageBox.setIcon(messageBox.Warning)
        messageBox.setWindowTitle("Message")
        messageBox.exec()
