
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

# SQLITE version: 3.11.0
# checking the version: select sqlite_version();//sql 

class ManageLocalStorage:

    def __init__(self,isConnected,connectionName):
        
        self.isConnected=isConnected
        self.connectionName=connectionName


    """
        QSqlDatabase is a class that has a static public member function called addDatabase that simply adds a database given the 
        driver type and the connection name. If there already exists a connection by the connection name provided in the function, that 
        connection is removed.

        the object db now has a few functions of its own that we can work on.
        setDatabaseName(), setUserName(), setPassword(), setHostName(), setPort(), setConnectOptions() and finally open(). 
        working of the functions is self-explanatory

        if no connection name is specified the new connection becomes the default connection

        if we add a connection with the same name as the existing connection the new connection replaces the old one.
    """
            
    def getConnectionName(self):
        
        return self.connectionName
    
    def setConnectionName(self,connectionName):
        
        self.connectionName=connectionName
        return True

    def getIsConnected(self):
        
        return self.isConnected

    def setIsConnected(self, isConnected):
        
        self.isConnected = isConnected


    def build(self):
        db = QSqlDatabase.addDatabase('QSQLITE',self.connectionName)
        
        db.setDatabaseName('PRLocalStorage')
        db.setUserName('ProjectRecommend')
        db.setPassword('elite1337')
        db.setPort(1337)

        """
        Error testing : whether the creation of database and opening of connection is successful or not
        """

        if not db.open():
            # db.open() returns true if the connection is open obviously
            print ("----------------------------------------------")
            print ("could not open the database")
            self.isConnected=False
            return False
        else:
            print ("----------------------------------------------")
            print ("opened the database successfully")
            self.isConnected=True

            #db=QSqlDatabase.database(self.connectionName)

            query = QSqlQuery(db)
           
            isQuerySuccessful=query.exec_("create table songs(SID int, SPath varchar(255), isUpdated int, TIT2 varchar(255), TALB varchar(255), TPE1 varchar(255), TPE2 varchar(255), TSOP varchar(255), TDRC date, TCON varchar(255),primary key(SID))")


            """
            isDeleteSuccessful=query.exec_("drop table if exists test")
            if isDeleteSuccessful:
                print ("table test dropped")
            else:
                print ("table could not be dropped:")
                print (query.lastError().text())
            isQuerySuccessful=query.exec_("create table test(SID int auto_increment primary key ,SPath varchar(255))")
            """

            # the fieldnames used here in the query are described in dbFields.md file in the same directory
            #know that this is how error information is grabbed in pyqt: QSqlDatabase
            
            """
            Error testing: whether the creation of the table is successful or not
            """

            if isQuerySuccessful:
                print("----------------------------------------------")
                print ("creation of table successful")

                #now that we have acatually created a table let us try inserting entries into that table
            else:
                print ("----------------------------------------------")
                print ("creation of table unsuccessful")
                error=query.lastError().text()
                print (error)   
            
            del query
            del db
            
            return True

    """
    build is working fine
    """

    """
    dumps the database
    returns true if the database exists and the database is successfully dumped
    returns false if the database does not exists 
    """

    def dump(self):
        
        """
        seems we cannot remove the database efficiently here so we need to essentially delete tables in the instance of the database already created
        """
        db=QSqlDatabase.database(self.connectionName,False)

        #just to close the connection I use False as the second parameter

        query=QSqlQuery(db)
        isDeleteSuccessful=query.exec_("drop table songs")
        
        if isDeleteSuccessful:
            print ("the table has been deleted successfully")
        else:
            print ("the table could not be deleted")
            print ("error:")
            print (query.lastError().text())

        del db

        return True
    
    def query(self):
        
        #sid, title, path, artist to be returned
        songDet={}

        db=QSqlDatabase.database(self.connectionName,True)
        #opening the connection
        query=QSqlQuery(db)
        SIDList=[]
        TitleList=[]
        SPathList=[]
        ArtistList=[]
        
        # SID, Title: TIT2, path:SPath , artist: TPE1
        isQuerySuccessful=query.exec_("select SID, SPath, TIT2, TPE1 from songs where 1=1")
        if isQuerySuccessful:
            print ("query is successful")
            while query.next():
                SIDList.append(query.value(0))
                TitleList.append(query.value(1))
                SPathList.append(query.value(2))
                ArtistList.append(query.value(3))

            songDet["SID"]=SIDList
            songDet["Title"]=TitleList
            songDet["SPath"]=SPathList
            songDet["Artist"]=ArtistList


            """
                songDet["SID"]=query.value(0)
                songDet["SPath"]=query.value(1)
                songDet["Title"]=query.value(2)
                songDet["Artist"]=query.value(3)
            """
        else:
            print ("query not successful")
            return {}

        return songDet


    def connect(self):
        db=QSqlDatabase.database(self.connectionName,True)
        print ("database name being connected and the connection names are as follows: ")
        print (db.databaseName())
        print (db.connectionName())
        del db
        self.isConnected=True

        return True

    def disconnect(self):
        db=QSqlDatabase.database(self.connectionName,False)
        print ("database name being disconnected and the connection names are as follows: ")
        print (db.databaseName())
        print (db.connectionName())
        del db
        self.isConnected=False

        return True

"""
error correction code follows, do not use during final implementation
"""

print ("Welcome to ManageLocalStorage, here are the following sets of commands: build, dump, connect, disconnect,-1 exiting")
obj=ManageLocalStorage(False,'sqLiteConProjectRecommendConnection') 
while True:
    
    x=str(input('input:')) # this is some python 3 stuff.
    
    if x=="build":
        if obj.build():
            print ("---------------------------------Success------------------------------")
        else:
            print ("---------------------------------Fail----------------------------------")
    elif x=="dump":
        if obj.dump():
            print ("---------------------------------Success------------------------------")
        else:
            print ("---------------------------------Fail------------------------------")
    elif x=="connect":
        if obj.connect():
            print ("---------------------------------Success------------------------------")
        else:
            print ("---------------------------------Fail------------------------------")
    elif x=="disconnect":
        if obj.disconnect():
            print ("---------------------------------Success------------------------------")
        else:
            print ("---------------------------------Fail------------------------------")
    elif x=="-1":
        break
    else:
        print ("incorrect command")
        

        
        

