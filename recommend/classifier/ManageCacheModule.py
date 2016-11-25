import sys
import GetRecommendation
from LocalStorage import AccessLocalStorage
from MusicPlayer import ManageSongs
from MusicPlayer import ControlMusic

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
        self.db = QSqlDatabase.database(connectionName,True)
        self.query = QSqlQuery(self.db)

    """
    Considering the documentation of the project we have an important function missing which builds the cache, so we are adding it here
    """

    def getConnectionName(self):
        return self.connectionName

    def setConnectionName(self, connectionName):
        self.connectionName = connectionName

    def buildCache(self):
        # buildCache is provided with the connectionName of the connection so that it is proper
        db = QSqlDatabase.addDatabase('QSQLITE', self.connectionName)
        db.setDatabaseName('PRCache')
        db.setUserName('ProjectRecommend')
        db.setPassword('elite1338')
        db.setPort(1338)

        if not db.isOpen():
            print("could not open the Cache database")
            return False
        else:
            print("opened the Cache database successfully")

        query = QSqlQuery(db)
        # for now i am not sure what is the data that will be stored in the cache and so i keep on SID and Spath for now

        isQuerySuccessful = query.exec_("create table songs(SID int, Title varchar(255),Artist varchar(255),URI varchar(255), Type boolean)")
        # URI will be the songPath in case the song is in the local PC and will be url in case the song is online

        if isQuerySuccessful:
            print("table successfully created")
            return False
        else:
            print("table could not be created")
            print("error:")
            print(query.lastError().text())

        # deleting these instances is important
        del db
        del query
        return True

    def ReadCache(self, songID):
        if self.db.isOpen():
            queryString = "SELECT SID, Title, Artist, URI, Type FROM songs WHERE SID="+str(songID)
            record = self.query.exec_(queryString)

            if record:
                print("read successfull ")
                a = 0
                while self.query.next():
                    print("executing times:")
                    print(a)
                    a = a+1
                    self.songDet["SID"] = self.query.value(0)
                    self.songDet["Title"] = self.query.value(1)
                    self.songDet["Artist"] = self.query.value(2)
                    self.songDet["URI"] = self.query.value(3)
                    self.songDet["Type"] = self.query.value(4)
            else:
                print("read unsuccessful")
                print("error")
                print(self.query.lastError().text())
        else:
            print("connection is not open")
            return False
        return self.songDet

    def WriteCache(self, predictedSong, songID):
        # predictedSong is a dictionary of lists having elements in the following order:
        # 1. Title, Artist, URI, Type
        # writing is only possible if connection is open
        
        if self.db.isOpen():
            # print("trying to write in DB")
            metadataDict=predictedSong
            self.query.prepare("insert into songs(SID, Title, Artist, URI, Type ) values(:SID, :Title, :Artist, :URI, :Type)")
            # SPath, isUpdated, TIT2, TALB, TPE1, TPE2, TSOP, TDRC, TCON, these are required, SID is auto incrimented
            self.query.bindValue(":SID",songID)
            self.query.bindValue(":Title", metadataDict.get("Title", "NULL"))
            self.query.bindValue(":Artist", metadataDict.get("Artist", "NULL"))
            self.query.bindValue(":URI", metadataDict.get("URI", "NULL"))
            self.query.bindValue(":Type", metadataDict.get("Type", "NULL"))

            if isQuerySuccessful:
                print("insertion successful")
                # print("no of rows affected: " + str(self.query.numRowsAffected()))
            elif self.query.lastError().number() is 19:
                pass
                # print("unique Construct failed")
                # print(self.query.lastError().number().text())
            else:
                print("insertion not successful")
                # print("error:")
                print(self.query.lastError().number())
                return False
        else:
            print("connection could not be established")
            return False
        return True


    def InvalidateCache(self):
        return False

    def dumpCache(self):
        db = QSqlDatabase.database(self.connectionName, False)
        # just to close the connection I use False as the second parameter
        query = QSqlQuery(db)
        isDeleteSuccessful = query.exec_("drop table songs")

        if isDeleteSuccessful:
            print("the table has been deleted successfully")
        else:
            print("the table could not be deleted")
            print("error:")
            print(query.lastError().text())
        del db
        return True

    def deleteCache(self, songID):
        if self.db.isOpen():
            isQuerySuccessful = query.exec_("delete from songs WHERE SID=" + str(songID))
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
