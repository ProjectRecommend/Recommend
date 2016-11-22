import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# SQLite version: 3.11.0
# check the SQLite version by running "select sqlite_version();" in SQLite


class ManageLocalStorage:

    def __init__(self, connectionName):
        self.isConnected = False
        self.connectionName = connectionName

    def getConnectionName(self):
        return self.connectionName

    def setConnectionName(self, connectionName):
        self.connectionName = connectionName
        return True

    # def getIsConnected(self):
    #     return self.isConnected
    # def setIsConnected(self, isConnected):
    #     self.isConnected = isConnected

    def build(self):
        db = QSqlDatabase.addDatabase('QSQLITE', self.connectionName)
        db.setDatabaseName('PRLocalStorage.sqlite3')
        db.setUserName('ProjectRecommend')
        db.setPassword('elite1337')
        db.setPort(1337)

        """
        Error testing : whether the creation of database and opening of connection is successful or not
        """

        if not db.open():
            # db.open() returns true if the connection is open obviously
            print("----------------------------------------------")
            print("could not open the database")
            self.isConnected = False
            return False
        else:
            print("----------------------------------------------")
            print("opened the database successfully")
            self.isConnected = True
            # db = QSqlDatabase.database(self.connectionName)
            query = QSqlQuery(db)
            isQuerySuccessful = query.exec_("create table songs(SID INTEGER PRIMARY KEY AUTOINCREMENT, SPath varchar(255) UNIQUE, isUpdated INTEGER, TIT2 varchar(255), TALB varchar(255), TPE1 varchar(255), TPE2 varchar(255), TSOP varchar(255), TDRC date, TCON varchar(255))")

            """
            Error testing: whether the creation of the table is successful or not
            """
            if isQuerySuccessful:
                print("creation of table successful")
            else:
                print("creation of table unsuccessful")
                error = query.lastError().text()
                print(error)
            # del query
            # del db
            return True

    """
    dumps the database
    returns true if the database exists and the database is successfully dumped
    returns false if the database does not exists
    """
    def dump(self):

        """
        seems we cannot remove the database efficiently here so we need to essentially delete tables in the instance of the database already created
        """
        # just to close the connection I use False as the second parameter
        db = QSqlDatabase.database(self.connectionName, False)
        query = QSqlQuery(db)
        isDeleteSuccessful = query.exec_("drop table songs")
        if isDeleteSuccessful:
            print("the table has been deleted successfully")
        else:
            print("the table could not be deleted")
            print("error:")
            print(query.lastError().text())
        # del db
        return True

    def query(self):
        # sid, title, path, artist to be returned
        songDet = {}
        db = QSqlDatabase.database(self.connectionName, True)
        # opening the connection
        query = QSqlQuery(db)
        SIDList = []
        TitleList = []
        SPathList = []
        ArtistList = []

        # SID, Title: TIT2, path:SPath , artist: TPE1
        isQuerySuccessful = query.exec_("select SID, SPath, TIT2, TPE1 from songs where 1=1")
        if isQuerySuccessful:
            print("query is successful")
            while query.next():
                SIDList.append(query.value(0))
                TitleList.append(query.value(1))
                SPathList.append(query.value(2))
                ArtistList.append(query.value(3))

            songDet["SID"] = SIDList
            songDet["Title"] = TitleList
            songDet["SPath"] = SPathList
            songDet["Artist"] = ArtistList
            """
                songDet["SID"]=query.value(0)
                songDet["SPath"]=query.value(1)
                songDet["Title"]=query.value(2)
                songDet["Artist"]=query.value(3)
            """
        else:
            print("query not successful")
            return {}

        return songDet

    def connect(self):
        db = QSqlDatabase.database(self.connectionName,True)
        print("database name being connected and the connection names are as follows: ")
        print(db.databaseName())
        print(db.connectionName())
        # del db
        self.isConnected = True
        return True

    def disconnect(self):
        db = QSqlDatabase.database(self.connectionName,False)
        print("database name being disconnected and the connection names are as follows: ")
        print(db.databaseName())
        print(db.connectionName())
        # del db
        self.isConnected = False
        return True
