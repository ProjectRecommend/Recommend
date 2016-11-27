import re
from PyQt5.QtSql import QSqlQuery
from Metadata.ManageMetaDataModule import ManageMetaData
from LocalStorage.ManageLocalStorageModule import ManageLocalStorage
import const
import discogs_client as dc

# ********************************** HARD CODED PART***************************

# client = dc.Client('test App', user_token="jQgfPZNxlkvrINfWvVjPrtbnfvAQLMrGeJHLyZeO")
# result = client.search(artist = 'Justin Bieber', type='relese', genre='pop', year='2010')

# RelevantSongDict = {}
# # return a dictionary of songs with relevant information
# # make a dictionary out of *result* object

# i = 0
# RelevantSongDict['songs'] = {}
# while(i < len(result)):
#     print('*********\n')
#     RelevantSongDict['songs'][i]={}
#     RelevantSongDict['songs'][i]['title'] = result[i].title
#     RelevantSongDict['songs'][i]['videos'] = result[i].videos
#     i = i+1
# print(RelevantSongDict)

# # **********************************END********************************


class GetRecommendation(object):

    def __init__(self, manageLocalStorage):
        # pass
        # don init stuff
        # self.mls = ManageLocalStorage(const.LS_connectionName)
        self.mls = manageLocalStorage

    def fetchRelevantSongOnline(self, SongMetaData):
        # This will store dictionary for songs information
        RelevantSongDict = {}

        # function taken from experiments/webAPI/testdc.py
        result = client.search(artist=SongMetaData.artist, type='release', genre=SongMetaData.genre, year=SongMetaData.year)

        # return a dictionary of songs with relevant information
        # make a dictionary out of *result* object

        i = 0
        RelevantSongDict['songs'] = {}

        # Building the dictionary
        while(i < len(result)):
            RelevantSongDict['songs'][i] = {}
            RelevantSongDict['songs'][i]['title'] = result[i].title
            RelevantSongDict['songs'][i]['videos'] = result[i].videos
            i = i+1

        return {RelevantSongDict}

    def fetchRelevantSongOffline(self, SongPath):
        print("in fetchRelevantSongOffline")
        metadataDict = {}
        year = ""
        relevantSong = []
        metadataDict = ManageMetaData.ReadMetaData(self, SongPath)
        # get year out of metadata TDRC tag
        if metadataDict.get("TDRC"):
            match = re.match(r'\d{4}', metadataDict.get("TDRC"))
            if match is not None:
                # it found a match!
                year = match.group(0)
        print(year)
        TPE1 = metadataDict.get("TPE1")
        print(metadataDict.get("TPE1"))
        # print(self.mls)
        # print(self.mls.db.databaseName())
        query = QSqlQuery(self.mls.db)
        queryString = "SELECT SPath FROM songs WHERE TPE1 = :TPE1 OR year = :year"
        if self.mls.db.open():
            print("db is open")
            query.prepare(queryString)
            query.bindValue(":TPE1", TPE1)
            query.bindValue(":year", year)
            print("executing queryString")
            record = query.exec_()
            # print(record)
            if record:
                print("read successful, it seems")
                while query.next():
                    relevantSong.append(query.value(0))
            else:
                print("read not successful")
                print("error")
                print(query.lastError().text())
                return False
        else:
            print("could not read from the database, connection not found")
            return False
        for path in relevantSong:
            print(path)


# SELECT column1, column2, columnN
# FROM table_name
# WHERE [condition1] OR [condition2]...OR [conditionN]

    def predict(self, SongPath, RelevantSongDict):
        return {}
