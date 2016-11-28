import re
import collections
from PyQt5.QtSql import QSqlQuery
from Metadata.ManageMetaDataModule import ManageMetaData
from LocalStorage.ManageLocalStorageModule import ManageLocalStorage
from classifier.cluster.algorithms.KMeans import kMeansClustering
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
        # list of path of all the relevant songs
        relevantSongPathList = []
        # dict that contains metadata of songs in paragraph as value and songPath as key
        relevantSongDict = {}
        # print("test")
        # print(SongPath)
        metadataDict = ManageMetaData.ReadMetaData(self, SongPath)
        # print(metadataDict)
        # get year out of metadata TDRC tag
        if metadataDict.get("TDRC"):
            match = re.match(r'\d{4}', metadataDict.get("TDRC"))
            if match is not None:
                # it found a match!
                year = match.group(0)
        # print(year)
        TPE1 = metadataDict.get("TPE1")
        # print(metadataDict.get("TPE1"))
        # print(self.mls)
        # print(self.mls.db.databaseName())
        query = QSqlQuery(self.mls.db)
        queryString = "SELECT SPath FROM songs WHERE TPE1 = :TPE1 OR year = :year"
        if self.mls.db.open():
            # print("db is open")
            query.prepare(queryString)
            query.bindValue(":TPE1", TPE1)
            query.bindValue(":year", year)
            print("executing queryString")
            record = query.exec_()
            # print(record)
            if record:
                # print("read successful, it seems")
                while query.next():
                    relevantSongPathList.append(query.value(0))
            else:
                # print("read not successful")
                print("error")
                print(query.lastError().text())
                return False
        else:
            print("could not read from the database, connection not found")
            return False
        # build relevantSongDict
        for path in relevantSongPathList:
            # print(path)
            relevantSongDict[path] = self.metadataToPara(path)
        # predict
        # if SongPath:
        #     self.predict(SongPath, relevantSongDict)
        # else:
        #     print("problem with SongPath so can't call predict")
        return relevantSongDict

    def predict(self, SongPath, relevantSongDict):
        # convert relevantSongDict to an OrderedDict
        # print(SongPath)
        # print("test")
        # print(relevantSongDict)
        relevantSongDict = collections.OrderedDict(relevantSongDict.items())
        # get index of song on which we are getting recommendations
        indexOfPlayingSong = list(relevantSongDict.keys()).index(SongPath)
        print("----- index of current song ----")
        print(indexOfPlayingSong)
        # make a list of metadata
        snippetsList = []
        for item in relevantSongDict:
            # print(relevantSongDict.get(item))
            snippetsList.append(relevantSongDict.get(item))
        # print("--------- predict data ------")
        # print("--------relevantSongDict-----------")
        # for item in relevantSongDict:
            # print(relevantSongDict.get(item))
        # print("---------snippetsList -------")
        # for i in range(len(snippetsList)):
            # print(snippetsList[i])
        # print("-------------KMeans-------------")
        # Magic happens here
        clusters = kMeansClustering(snippetsList)
        clusters.find_clusters(4)
        # print(clusters.get_common_phrases(2))
        clusters.print_clusters()
        clusters_dict = clusters.get_clusters()
        # print(clusters_dict)
        # print(len(clusters_dict))
        # for i in range(len(clusters_dict)):
        #     print("\n")
        #     print("cluster Number : " + str(i))
        #     cluster_items = clusters_dict.get(i+1)
        #     for item in cluster_items:
        #         print("item number : " + str(item), end=' ')
        #         print(snippetsList[item])
        # print("----------------")
        # print("playing song")
        # print(snippetsList[indexOfPlayingSong])
        # print(relevantSongDict.get(SongPath))
        # print(list(relevantSongDict)[indexOfPlayingSong])
        # detect cluster that have our song
        final_cluster = ""
        suggestedSongsPath = []
        for key in clusters_dict:
            item = clusters_dict.get(key)
            # print(item)
            if indexOfPlayingSong in item:
                final_cluster = item
                # print(item)
                # print(key)
        print("---- suggested songs ----")
        print(final_cluster)
        # use indexes of suggested songs and make a list of path of suggested songs
        for index in final_cluster:
            suggestedSongsPath.append(list(relevantSongDict)[index])
            # print(list(relevantSongDict)[index])
        return suggestedSongsPath

    def metadataToPara(self, SongPath):
        # print(SongPath)
        metadataDict = ManageMetaData.ReadMetaData(self, SongPath)
        text = ""
        for item in metadataDict:
            text = text + metadataDict.get(item) + " "
        # print(text)
        return text
