import os

# this module provides a portable way of using operating system dependent
# functionality, file manipulations for example.
# import loloLyrics module
from Metadata import loloLyrics

# metadata module
from Metadata.tags import getTags 
from Metadata.tagsReadMetadata import getMetadataDict
from Metadata.loloLyrics import getLyrics

# TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT

from mutagen.id3 import (USLT, TIT2, TPE1, TPE2, TALB, TSOP, TCON, TDRC)
from mutagen.id3 import ID3

# FIXED_VARIABLES FOR TESTING PURPOSES
# ROOT_DIR = '/home/raghav/nu/ProjectRecommand/experiments/AddLyrics'
# FILE_NAME = 'xxx.mp3'


"""--------Parameter: Lyrics-------- """

# For Lyrics the user does not add any metadata, it can be fetched from lololyrics.


class EditLyrics(object):
    def __init__(self, filePath):
        self.obj=getTags(filePath)
        pass

    # Function to check if file contains lyrics or not
    # Returns 0 if it contains less than 15 words in Lyrics else returns 1
    def ifLyrics(self, filePath):
        # filePath = os.path.join(root_dir, fileName)

        lyrics = self.obj.getLyricsMetadata() # list of elements
        # Assuming that a song can't have lyrics lesses than 15 words
        if(len(lyrics)<15):
            print(0)
            return(0)
        else:
            print(1)
            return(1)

    # remove lyrics form corresponding ID3 tag from file
    def removeLyrics(self, filePath):
        # filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)
        audio.delall('USLT')
        audio.add(USLT(encoding=3, text=u" "))
        return audio.save()

    # fetch lyrics and add to corresponding ID3 tag from file
    def addLyrics(self, filePath):
        # filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)
        audio.add(USLT(encoding=3, text=self.fetchLyrics(filePath)))
        return audio.save()

    # fetches lyrics from lololyrics.com
    def fetchLyrics(self, file_path):
        artist = self.obj.getArtistMetadata()
        title = self.obj.getTitleMetadata()
        return(loloLyrics.getLyrics(artist, title))

    def writeLyrics(self, filePath):
        if(self.ifLyrics(filePath) == 0):
            self.removeLyrics(filePath)
            print("** removeLyrics function done **")
            self.addLyrics(filePath)
            print("** addLyrics function done **")
        elif(self.ifLyrics(filePath) == 1):
            print("***ALL OK ***")

"""----------Edit rest of the tags-----------------"""
# TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT

# title, album, Lead performer, band, performer sort order, year, content type, lyrics
# tag names: title, album, lead, band, performerSortOrder, year, contentType

# TIT2 is Title of the song.


class EditMetadata(object):
    def __init__(self, filePath):
        self.metaDict = {}
        self.obj=getTags(filePath)

    # def ifTag(self, tag):
    #     # filePath = os.path.join(root_dir, fileName)
        
    #     if tag == "TIT2":
    #         # TIT2:title
    #         title = self.obj.getTitleMetadata()
    #         if (len(title) == 0):
    #             print(0)
    #             return 0
    #         else:
    #             print(1)
    #             return 1
    #     elif tag == "TALB":
    #         # TALB:album
    #         album = self.obj.getAlbumMetadata()
    #         if(len(album) == 0):
    #             print(0)
    #             return 0
    #         else:
    #             print(1)
    #             return 1
    #     elif tag == "TPE1":
    #         # TPE1:Lead
    #         lead = self.obj.getLeadMetadata()
    #         if (len(lead)):
    #             print(0)
    #             return 0
    #         else:
    #             print(1)
    #             return 1
    #     elif tag == "TPE2":
    #         # TPE2:band
    #         band = self.obj.getBandMetadata()
    #         if (len(band)):
    #             print(0)
    #             return 0
    #         else:
    #             print(1)
    #             return 1
    #     elif tag == "TSOP":
    #         # TSOP:performer sort order.
    #         pso = self.obj.getPSOMetadata()
    #         if (len(pso)):
    #             print(0)
    #             return 0
    #         else:
    #             print(1)
    #             return 1
    #     elif tag == "TDRC":
    #         # TDRC: year
    #         year = self.obj.getYearMetadata()
    #         if (len(year)):
    #             print(0)
    #             return 0
    #         else:
    #             print(1)
    #             return 1
    #     elif tag == "TCON":
    #         # TCON: Content type
    #         cType = self.obj.getCTypeMetadata()
    #         if (len(cType)):
    #             print(0)
    #             return 0
    #         else:
    #             print(1)
    #             return 1
    #     else:
    #         print("error")

    # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT
    # tag names: title, album, lead, band, performerSortOrder, year, contentType

    # remove lyrics form corresponding ID3 tag from file
    def removeTag(self, filePath, tag):
        # filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)
        if tag == "TIT2":
            audio.delall('TIT2')
            audio.add(TIT2(encoding=3, text=u" "))

        elif tag == "TALB":
            audio.delall('TALB')
            audio.add(TALB(encoding=3, text=u" "))

        elif tag == "TPE1":
            audio.delall('TPE1')
            audio.add(TPE1(encoding=3, text=u" "))

        elif tag == "TPE2":
            audio.delall('TPE2')
            audio.add(TPE2(encoding=3, text=u" "))

        elif tag == "TSOP":
            audio.delall('TSOP')
            audio.add(TSOP(encoding=3, text=u" "))

        elif tag == "TDRC":
            audio.delall('TDRC')
            audio.add(TDRC(encoding=3, text=u" "))

        elif tag == "TCON":
            audio.delall('TCON')
            audio.add(TCON(encoding=3, text=u" "))

        else:
            print("error: tag unidentified")
            return "error"
        return audio.save()


    # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT
    # tag names: title, album, lead, band, performerSortOrder, year, contentType

    # fetch lyrics and add to corresponding ID3 tag from file
    def addTag(self, filePath, songMetadata, tag):
        # filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)

        if tag == "TIT2":
            audio.add(TIT2(encoding=3, text=self.fetchTag(songMetadata,tag)))
        elif tag == "TALB":
            audio.add(TALB(encoding=3, text=self.fetchTag(songMetadata,tag)))
        elif tag == "TPE1":
            audio.add(TPE1(encoding=3, text=self.fetchTag(songMetadata,tag)))
        elif tag == "TPE2":
            audio.add(TPE2(encoding=3, text=self.fetchTag(songMetadata,tag)))
        elif tag == "TSOP":
            audio.add(TSOP(encoding=3, text=self.fetchTag(songMetadata,tag)))
        elif tag == "TDRC":
            audio.add(TDRC(encoding=3, text=self.fetchTag(songMetadata,tag)))
        elif tag == "TCON":
            audio.add(TCON(encoding=3, text=self.fetchTag(songMetadata,tag)))
        else:
            print("error: tag not recognized")
            return "error"

        return audio.save()
    # fetches lyrics from lololyrics.com
    # def fetchLyrics(self,file_path):
    #     artist = getArtistMetadata(file_path)
    #     title = getTitleMetadata(file_path)
    #     return(loloLyrics.getLyrics(artist, title))

    # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT
    # tag names: title, album, lead, band, performerSortOrder, year, contentType

    # get function of dictionary: get(arg1,arg2), arg1 is the key to get and arg2 is returned if None is found corresponding
    # to arg1

    def fetchTag(self, songMetadata, tag):
        print ("inside fetchTag:\n")
        print (songMetadata)
        if tag == "TIT2":
            return songMetadata.get("TIT2"," ")
        elif tag == "TALB":
            return songMetadata.get("TALB"," ")
        elif tag == "TPE1":
            return songMetadata.get("TPE1"," ")
        elif tag == "TPE2":
            return songMetadata.get("TPE2"," ")
        elif tag == "TSOP":
            return songMetadata.get("TSOP"," ")
        elif tag == "TDRC":
            return songMetadata.get("TDRC"," ")
        elif tag == "TCON":
            return songMetadata.get("TCON"," ")
        else:
            print("error: tag unidentified")
            return "error"

    # songMetadata is an object of ManageMetaData  class
    def writeTag(self, filePath, tag):
        # dereferencing the songMetadata object and storing it in a dictionary
        # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT
        # tag names: title, album, lead, band, performerSortOrder, year, contentType
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
        print ("metaDict currently:\n")
        print (self.metaDict)
        # isTagPresent=self.ifTag(tag)
        # if( isTagPresent == 0):
        if self.metaDict.get(tag)!=None:
            self.removeTag(filePath, tag)
            print("** removeTag function done **")
            self.addTag(filePath, self.metaDict, tag)
            print("** addTag function done **")
        # elif( isTagPresent == 1):
        #     print("***ALL OK ***")

    def populateMetadict(self, songMetadata):
        # self.metaDict["TPE1"] = songMetadata.artistTPE1
        # self.metaDict["TPE2"] = songMetadata.artistTPE2
        # self.metaDict["TIT2"] = songMetadata.titleTIT2
        # self.metaDict["TALB"] = songMetadata.albumTALB
        # self.metaDict["TSOP"] = songMetadata.artistTSOP
        # self.metaDict["TDRC"] = songMetadata.recDateTDRC
        # self.metaDict["TCON"] = songMetadata.genreTCON
        self.metaDict["TPE1"] = songMetadata.artistTPE1
        self.metaDict["TPE2"] = songMetadata.artistTPE2
        self.metaDict["TIT2"] = songMetadata.titleTIT2
        self.metaDict["TALB"] = songMetadata.albumTALB
        self.metaDict["TSOP"] = songMetadata.artistTSOP
        self.metaDict["TDRC"] = songMetadata.recDateTDRC
        self.metaDict["TCON"] = songMetadata.genreTCON
        

