from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
from Metadata.ManageMetaDataModule import ManageMetaData
from LocalStorage.ManageLocalStorageModule import ManageLocalStorage


"""
WARNING: Do not initialize 2 separate instances of QSqlDatabase class while handling the database actions
"""


class AccessLocalStorage(object):
    def __init__(self, connectionName):
        # the second parameter also opens the connection if the connection is not already open
        self.db = QSqlDatabase.database(connectionName, True)
        # print("current connectionName:")
        # print(self.db.connectionName())
        self.query = QSqlQuery(self.db)
        self.songDict = {}
        # so basically querying on the instance of the database mentioned earlier

    """
    The database function simply returns an instance of the connection given the connection name. The second parameter is a boolean
    value that tells us whether the connection is open or not, if the connection is not already open, it is opened now.
    """

    def read(self, SongID):
        if self.db.isOpen():
            """
            QSqlQuery(const QString &query = QString(), QSqlDatabase db = QSqlDatabase())
            accepts a query string and a database instance (of class QSqlDatabase) and the object can be
            used for simply navigating the record(if select statement is used).
            """
            # queryString="SELECT SID, SPath, isUpdated FROM songs WHERE SID=" + str(songID)
            # record=self.query.exec_(queryString)
            queryString = "SELECT SID, SPath, isUpdated, TIT2, TALB, TPE1, TPE2, TSOP, TDRC, TCON FROM songs WHERE SongID=" + str(SongID)
            record = self.query.exec_(queryString)
            # now we can use record object (which is an QSqlQuery object) to navigate the record
            if record:
                print("read successful, it seems")
                a = 0
                while self.query.next():
                    print("executing times: ")
                    print(a)
                    a = a + 1
                    self.songDict["SID"] = self.query.value(0)
                    self.songDict["SPath"] = self.query.value(1)
                    self.songDict["isUpdated"] = self.query.value(2)
                    self.songDict["TIT2"] = self.query.value(3)
                    self.songDict["TALB"] = self.query.value(4)
                    self.songDict["TPE1"] = self.query.value(5)
                    self.songDict["TPE2"] = self.query.value(6)
                    self.songDict["TSOP"] = self.query.value(7)
                    self.songDict["TDRC"] = self.query.value(8)
                    self.songDict["TCON"] = self.query.value(9)
            else:
                print("read not successful")
                print("error")
                print(self.query.lastError().text())
                return False
        else:
            print("could not read from the database, connection not found")
            return False
        return self.songDict
    """
    the following function writes song details, like its metadata and so on into the database, it is
    passed the songPath only, it calls the function ReadMetaData which returns a dictionary containing key value
    pairs of the songMetadata
    """

    def write(self, SongPath):
        # print(SongPath)
        if self.db.isOpen():
            print("trying to write in DB")
            songDict = {}
            songDict = ManageMetaData.ReadMetaData(self, SongPath)
            print("inside AccessLocalStorage ")
            print(songDict)
            # this will read metadata songPath.
            """
            the songDict format is always the same
            """
            valuesList = songDict.values()
            print(valuesList)
            valuesString = ""
            for i in range(9):
                if not i == 8:
                    valuesString = valuesString + valuesList[i] + ","
                    print(valuesString)
                else:
                    valuesString = valuesString+valuesList[i]
            queryString = "select * from songs"
            record = self.query.exec_(queryString)
            size = 0

            while self.query.next():
                size = size + 1

            valuesString = str(size+1) + "," + valuesString

            queryString = "insert into songs (SID,SPath,isUpdated,TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON) values (" + valuesString + ")"
            isQuerySuccessful = query.exec_(queryString)
            if isQuerySuccessful:
                print("----------------------------------------------")
                print("insertion successful")
                print("no of rows affected: " + str(self.query.numRowsAffected()))
            else:
                print("----------------------------------------------")
                print("insertion not successful")
                print("error:")
                print(self.query.lastError().text())
                return False
        else:
            print("connection could not be established")
            return False
        return True

    def delete(self, SongID):
        if self.db.isOpen():
            isQuerySuccessful = query.exec_("delete from songs WHERE SID=" + str(SongID))
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

    def getSongPath(self):
        return SongPath

    def setSongPath(self, SongPath):
        self.songPath = songPath
    """
    the following function is only for the purpose of testing purpose, delete this function for release
    """

    def testQueries(self, queryInstance, query):
        queryInstance.exec_(query)

# print ("Welcome to AccessLocalStorage terminal, this terminal lets you build a database with song table and read and write data to it")
# print ("commands: build, dump, disconnect, connect, read, write, delete")

