from Metadata.LyricsAndMetaData import EditLyrics, EditMetadata
from Metadata import tagsReadMetadata
from Metadata import tags


class ManageMetaData(object):
    def __init__(self):
        # don init stuff
        # self.SongMetaData = None
        # implement member var stuff

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
        # this function simply trys to get the metadata from the song and return it if it is found.
        # the tags python file contains the necessary functions to read metadata from the song and return it in the form of both
        # a dictionary and a list
        metadataDict = {}
        metadataDict = tagsReadMetadata.getMetadataDict(SongPath)
        # SongPath is the absolute song path.
        # for example: "D://Songs(english)//naked//Bony_M_Jingle_Bells.mp3", the // are necessary here
        metadataDict = tagsReadMetadata.metaDataDictToUnicode(metadataDict)
        # here metadataDict returns the following parameters: TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT
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
        # print(metadataDict)
        # always prefer dict.get(key) over dict[key], it won't raise KeyError
        # and can set default if value not found, if no default supplied it's None
        self.artistTPE1 = metadataDict.get("TPE1")
        self.artistTPE2 = metadataDict.get("TPE2")
        self.albumTALB = metadataDict.get("TALB")
        self.artistTSOP = metadataDict.get("TSOP")
        self.lyricsUSLT = metadataDict.get("USLT")
        self.recDateTDRC = metadataDict.get("TDRC")
        self.releaseTDOR = metadataDict.get("TDOR")
        self.publisherTPUB = metadataDict.get("TPUB")
        self.titleTIT2 = metadataDict.get("TIT2")
        self.genreTCON = metadataDict.get("TCON")

        return metadataDict

    def WriteMetaData(self, SongPath):
        # WriteMetaData is called when
        # this function writes metadata into the song.
        rootDir = ""
        fileName = ""
        # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON
        obj = EditMetaData()
        obj.populateMetadict(self)
        obj.writeTag(SongPath, "TIT2")
        obj.writeTag(SongPath, "TALB")
        obj.writeTag(SongPath, "TPE1")
        obj.writeTag(SongPath, "TPE2")
        obj.writeTag(SongPath, "TSOP")
        obj.writeTag(SongPath, "TDRC")
        obj.writeTag(SongPath, "TCON")
        obj = EditLyrics()
        obj.writeLyrics(SongPath)
        return False

    def FetchMetaDataFromMusicBrainz(self, SongMetaData):
        # this function temporarily remains un implemented.
        return {}

    def EditMetaData(self, SongPath):
        # function already implemented in WriteMetaData
        return False

