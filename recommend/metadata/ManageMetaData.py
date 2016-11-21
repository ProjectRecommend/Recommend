from MetadataMod import tags 
from AddLyricsMod import main

class ManageMetaData(object):
    def __init__(self):
        # don init stuff
        self.SongMetaData = None
        # impliment member var stuff

    def ReadMetaData(self, SongPath):
        #this function simply trys to get the metadata from the song and return it if it is found.
        
        #the tags python file contains the necessary functions to read metadata from the song and return it in the form of both 
        #a dictionary and a list

        metadataDict=getMetadataDict(SongPath)

        #SongPath is the absolute song path.
        # for example: "D://Songs(english)//naked//Bony_M_Jingle_Bells.mp3", the // are necessary here

        metadataDict=metaDataDictToUnicode(metadataDict)        

        #here metadataDict returns the following parameters: TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT
        self.SongMetaData=metadataDict
        return metadataDict

    def WriteMetaData(self, SongPath, SongMetaData):
        # this function writes metadata into the song.
        return False

    def FetchMetaDataFromMusicBrainz(self, SongMetaData):
        return {}

    def EditMetaData(self, SongPath):
        return False

    def getSongMetaData(self):
        return self.SongMetaData

    def setSongMetaData(self, SongMetaData):
        
        self.SongMetaData=SongMetaData
        return True
