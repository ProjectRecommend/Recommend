from LyricsAndMetaData import EditLyrics, EditMetadata
import tagsReadMetaData
import tags


class ManageMetaData(object):
    def __init__(self):
        # don init stuff
        # self.SongMetaData = None
        # impliment member var stuff

        self.artistTPE1 = None
        self.artistTPE2 = None
        self.albumTALB = None
        self.artistTSOP = None
        self.lyricsUSLT = None
        self.recDateTDRC = None
        self.releaseTDOR = None
        self.publisherTPUB = None
        self.titleTIT2 = None
        self.genreTCON = None

    def ReadMetaData(self, SongPath):
        #this function simply trys to get the metadata from the song and return it if it is found.

        #the tags python file contains the necessary functions to read metadata from the song and return it in the form of both
        #a dictionary and a list

        metadataDict=getMetadataDict(SongPath)

        #SongPath is the absolute song path.
        # for example: "D://Songs(english)//naked//Bony_M_Jingle_Bells.mp3", the // are necessary here

        metadataDict=metaDataDictToUnicode(metadataDict)

        #here metadataDict returns the following parameters: TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT


        # populating SongMetadata object

        #     def __init__(self):
        #     self.artistTPE1 = None
        # self.artistTPE2 = None
        # self.albumTALB = None
        # self.artistTSOP = None
        # self.lyricsUSLT = None
        # self.recDateTDRC = None
        # self.releaseTDOR = None
        # self.publisherTPUB = None
        # self.titleTIT2 = None
        # self.genreTCON = None

        self.artistTPE1=metadataDict["TPE1"]
        self.artistTPE2=metadataDict["TPE2"]
        self.albumTALB=metadataDict["TALB"]
        self.artistTSOP=metadataDict["TSOP"]
        self.lyricsUSLT=None
        self.recDateTDRC=metadataDict["TDRC"]
        self.releaseTDOR=None
        self.publisherTPUB=metadataDict["TPUB"]
        self.titleTIT2=metadataDict["TIT2"]
        self.genreTCON=metadataDict["TCON"]

        # self.SongMetaData=metadataDict
        return metadataDict

    def WriteMetaData(self, SongPath):
        # WriteMetaData is called when
        # this function writes metadata into the song.

        rootDir=""
        fileName=""

        # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON

        obj=EditMetaData()
        obj.populateMetadict(self)
        obj.writeTag(SongPath,"TIT2")
        obj.writeTag(SongPath,"TALB")
        obj.writeTag(SongPath,"TPE1")
        obj.writeTag(SongPath,"TPE2")
        obj.writeTag(SongPath,"TSOP")
        obj.writeTag(SongPath,"TDRC")
        obj.writeTag(SongPath,"TCON")

        obj=EditLyrics()
        obj.writeLyrics(SongPath)

        return False

    def FetchMetaDataFromMusicBrainz(self, SongMetaData):
        # this function temporarily remains un implemented.
        return {}

    def EditMetaData(self, SongPath):
        # function already implemented in WriteMetaData
        return False

