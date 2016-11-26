from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import sys,os
path=os.getcwd()
path=path[:-12]
sys.path.insert(1,path)
from Metadata.ManageMetaDataModule import ManageMetaData
from LocalStorage.ManageLocalStorageModule import ManageLocalStorage


"""
WARNING: Do not initialize 2 separate instances of QSqlDatabase class while handling the database actions
"""

class AccessLocalStorage(object):
    def __init__(self, connectionName):
        """
        The QSqlDatabase.database function simply returns an instance of the connection given the connection name. The second parameter is a boolean
        value that tells us whether the connection is open or not, if the connection is not already open, it is opened now.
        the second parameter also opens the connection if the connection is not already open
        """
        self.db = QSqlDatabase.database(connectionName, True)
        # print("current connectionName:")
        # print(self.db.connectionName())
        self.query = QSqlQuery(self.db)
        self.songDict = {}
        # so basically querying on the instance of the database mentioned earlier

    def read(self, SongPath):
        if self.db.isOpen():
            """
            QSqlQuery(const QString &query = QString(), QSqlDatabase db = QSqlDatabase())
            accepts a query string and a database instance (of class QSqlDatabase) and the object can be
            used for simply navigating the record(if select statement is used).
            """
            # queryString="SELECT SID, SPath, isUpdated FROM songs WHERE SID=" + str(songID)
            # record=self.query.exec_(queryString)
            queryString = "SELECT SID, SPath, isUpdated, TIT2, TALB, TPE1, TPE2, TSOP, TDRC, TCON FROM songs WHERE SPath = :SongPath" 
            self.query.prepare(queryString)
            self.query.bindValue(":SongPath",SongPath)
            record=self.query.exec_()
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
            # print("trying to write in DB")
            metadataDict = {}
            metadataDict = ManageMetaData.ReadMetaData(self, SongPath)
            """
            songDict come in undefined order always,we make a ordered list out of it.
            so we can iterate and insert it in db as it in db schema
            order of elements in db table/schema
            SID, SPath, isUpdated, TIT2, TALB, TPE1, TPE2, TSOP, TDRC, TCON
            """
            self.query.prepare("insert into songs(SPath, isUpdated, TIT2, TALB, TPE1, TPE2, TSOP, TDRC, TCON ) values(:SPath, :isUpdated, :TIT2, :TALB, :TPE1, :TPE2, :TSOP, :TDRC, :TCON)")
            # SPath, isUpdated, TIT2, TALB, TPE1, TPE2, TSOP, TDRC, TCON, these are required, SID is auto incrimented
            self.query.bindValue(":SPath", SongPath)
            self.query.bindValue(":isUpdated", 0)
            self.query.bindValue(":TIT2", metadataDict.get("TIT2", "NULL"))
            self.query.bindValue(":TALB", metadataDict.get("TALB", "NULL"))
            self.query.bindValue(":TPE1", metadataDict.get("TPE1", "NULL"))
            self.query.bindValue(":TPE2", metadataDict.get("TPE2", "NULL"))
            self.query.bindValue(":TSOP", metadataDict.get("TSOP", "NULL"))
            self.query.bindValue(":TDRC", metadataDict.get("TDRC", "NULL"))
            self.query.bindValue(":TCON", metadataDict.get("TCON", "NULL"))
            isQuerySuccessful = self.query.exec_()

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

    def delete(self, SongPath):
        if self.db.isOpen():
            
            self.query.prepare("delete from songs WHERE SID=:SongPath")
            self.query.bindValue(":SongPath",SongPath)
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

    def update(self, SongPath):
        if self.db.isOpen():
            # print("trying to write in DB")
            metadataDict = {}
            metadataDict = ManageMetaData.ReadMetaData(self, SongPath)
            """
            songDict come in undefined order always,we make a ordered list out of it.
            so we can iterate and insert it in db as it in db schema
            order of elements in db table/schema
            SID, SPath, isUpdated, TIT2, TALB, TPE1, TPE2, TSOP, TDRC, TCON
            """
            self.query.prepare("update songs SET isUpdated=:isUpdated, TIT2=:TIT2, TALB=:TALB, TPE1=:TPE1, TPE2=:TPE2, TSOP=:TSOP, TDRC=:TDRC, TCON=:TCON WHERE SPath=:SPath")
            # SPath, isUpdated, TIT2, TALB, TPE1, TPE2, TSOP, TDRC, TCON, these are required, SID is auto incrimented
            self.query.bindValue(":SPath", SongPath)
            self.query.bindValue(":isUpdated", 1)
            self.query.bindValue(":TIT2", metadataDict.get("TIT2", "NULL"))
            self.query.bindValue(":TALB", metadataDict.get("TALB", "NULL"))
            self.query.bindValue(":TPE1", metadataDict.get("TPE1", "NULL"))
            self.query.bindValue(":TPE2", metadataDict.get("TPE2", "NULL"))
            self.query.bindValue(":TSOP", metadataDict.get("TSOP", "NULL"))
            self.query.bindValue(":TDRC", metadataDict.get("TDRC", "NULL"))
            self.query.bindValue(":TCON", metadataDict.get("TCON", "NULL"))
            isQuerySuccessful = self.query.exec_()

            if isQuerySuccessful:
                print("update successful")
                # print("no of rows affected: " + str(self.query.numRowsAffected()))
            else:
                print("update not successful")
                # print("error:")
                print(self.query.lastError().number())
                return False
        else:
            print("connection could not be established")
            return False
        return True

