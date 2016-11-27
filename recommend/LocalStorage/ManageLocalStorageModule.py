import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel

# SQLite version: 3.11.0
# check the SQLite version by running "select sqlite_version();" in SQLite


class ManageLocalStorage(object):
    def __init__(self, connectionName):
        self.isConnected = False
        self.connectionName = connectionName
        self.db = QSqlDatabase.addDatabase('QSQLITE', self.connectionName)

    # def getConnectionName(self):
    #     return self.connectionName
    # def setConnectionName(self, connectionName):
    #     self.connectionName = connectionName
    #     return True
    # def getIsConnected(self):
    #     return self.isConnected
    # def setIsConnected(self, isConnected):
    #     self.isConnected = isConnected

    def build(self):
        self.db.setDatabaseName('PRLocalStorage.sqlite3')
        self.db.setUserName('ProjectRecommend')
        self.db.setPassword('elite1337')
        self.db.setPort(1337)

        """
        Error testing : whether the creation of database and opening of connection is successful or not
        """

        if not self.db.open():
            # db.open() returns true if the connection is open obviously
            print("could not open the database")
            self.isConnected = False
            return False
        else:
            print("opened the database successfully")
            self.isConnected = True
            # db = QSqlDatabase.database(self.connectionName)
            query = QSqlQuery(self.db)
            isQuerySuccessful = query.exec_("create table songs(SID INTEGER PRIMARY KEY AUTOINCREMENT, SPath varchar(255) UNIQUE, isUpdated INTEGER, TIT2 varchar(255), TALB varchar(255), TPE1 varchar(255), TPE2 varchar(255), TSOP varchar(255), TDRC date, TCON varchar(255), year varchar(255))")

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
        query = QSqlQuery(self.db)
        isDeleteSuccessful = query.exec_("drop table songs")
        if isDeleteSuccessful:
            print("the table has been deleted successfully")
        else:
            print("the table could not be deleted")
            print("error:")
            print(query.lastError().text())
        return True

    def query(self):
        projectModel = QSqlQueryModel()
        if self.db.open():
            projectModel.setQuery("select SID, SPath, TIT2, TSOP from songs", self.db)
            # print(dir(projectModel))
        else:
            print("Query failed")
        return projectModel

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
