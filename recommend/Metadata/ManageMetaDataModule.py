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
        # metadataDict = tagsReadMetadata.metaDataDictToUnicode(metadataDict)

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
        # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON

        # self.populate(songMetadata)

        metaDataobj = EditMetadata(SongPath)
        metaDataobj.populateMetadict(self)

        metaDataobj.writeTag(SongPath, "TIT2")
        print ("TIT2 done\n")
        metaDataobj.writeTag(SongPath, "TALB")
        print ("TALB done\n")
        metaDataobj.writeTag(SongPath, "TPE1")
        print ("TPE1 done\n")
        metaDataobj.writeTag(SongPath, "TPE2")
        print ("TPE2 done\n")
        metaDataobj.writeTag(SongPath, "TSOP")
        print ("TSOP done\n")
        metaDataobj.writeTag(SongPath, "TDRC")
        print ("TDRC done\n")
        metaDataobj.writeTag(SongPath, "TCON")
        print ("TCON done\n")
        print ("All tags except USLT done")
        # lyricsObj = EditLyrics(SongPath)
        # lyricsObj.writeLyrics(SongPath)
        return True

        

