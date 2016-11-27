# ********************************** HARD CODED PART***************************
import discogs_client as dc

client = dc.Client('test App', user_token="jQgfPZNxlkvrINfWvVjPrtbnfvAQLMrGeJHLyZeO")
result = client.search(artist = 'Justin Bieber', type='relese', genre='pop', year='2010')

RelevantSongDict = {}
# return a dictionary of songs with relevant information
# make a dictionary out of *result* object

i = 0
RelevantSongDict['songs'] = {}
while(i < len(result)):
    print('*********\n')
    RelevantSongDict['songs'][i]={}
    RelevantSongDict['songs'][i]['title'] = result[i].title
    RelevantSongDict['songs'][i]['videos'] = result[i].videos
    i = i+1
print(RelevantSongDict)

# **********************************END*****************************************

# *****************ACTUAL PART**************************************************


class GetRecommendation(object):

    def __init__(self):
        # don init stuff
        pass

    def FetchRelevantSongOnline(self, SongMetaData):
        # This will store dictionary for songs information
        RelevantSongDict = {}

        # function taken from experiments/webAPI/testdc.py
        result = client.search(artist = SongMetaData.artist, type='release', genre=SongMetaData.genre, year=SongMetaData.year)

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

    def FetchRelevantSongOffline(self, SongPath):
        metadataDict = {}
        year = ""
        metadataDict = ManageMetaData.ReadMetaData(self, SongPath)
        # get year out of metadata's TDRC tag
        if metadataDict.get("TDRC"):
            match = re.match(r'\d{4}', metadataDict.get("TDRC"))
            if match is not None:
                # it found a match!
                year = match.group(0)
        # print(year)
        

    def Predict(self, SongMetaData, RelevantSongDict):
        return {}
