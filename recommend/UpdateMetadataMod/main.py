# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:17:21 2016
"""
import os

#this module provides a portable way of using operating system dependent functionality, file manipulations for example.

# import loloLyrics module
import loloLyrics

# metadata module
from tags import (getLyricsMetadata, getArtistMetadata, getTitleMetadata, getAlbumMetadata, getLeadMetadata, getBandMetadata, getPSOMetadata, getYearMetadata, getCTypeMetadata)

from mutagen.id3 import USLT
from mutagen.id3 import ID3
from songMetadataObject import SongMetadata

# FIXED_VARIABLES FOR TESTING PURPOSES
# ROOT_DIR = '/home/raghav/nu/ProjectRecommand/experiments/AddLyrics'
# FILE_NAME = 'xxx.mp3'


"""-------------------------------------------------------Parameter: Lyrics------------------------------------------------------- """

# For Lyrics the user does not add any metadata, it can be fetched from lololyrics.

class EditLyrics:

    def __init__(self):
        
    # Function to check if file contains lyrics or not
    # Returns 0 if it contains less than 15 words in Lyrics else returns 1
    def ifLyrics(self,root_dir, fileName):
        filePath = os.path.join(root_dir, fileName)
        lyrics = getLyricsMetadata(filePath) # list of elements    
        # Assuming that a song can't have lyrics lesses than 15 words
        if(len(lyrics)<15):
            print(0)
            return(0)
        else: 
            print(1)
            return(1)
        
    # remove lyrics form corresponding ID3 tag from file
    def removeLyrics(self,root_dir, file_name):
        filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)
        audio.delall('USLT')
        audio.add(USLT(encoding=3, text=u" "))
        return audio.save()
        
    # fetch lyrics and add to corresponding ID3 tag from file
    def addLyrics(self,root_dir, file_name):
        filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)
        audio.add(USLT(encoding=3, text=fetchLyrics(filePath)))
        return audio.save()

    # fetches lyrics from lololyrics.com
    def fetchLyrics(self,file_path):
        artist = getArtistMetadata(file_path)
        title = getTitleMetadata(file_path)
        return(loloLyrics.getLyrics(artist, title))
        

    def writeLyrics(self,ROOT_DIR,FILE_NAME):
        if(ifLyrics(ROOT_DIR, FILE_NAME) == 0):
            removeLyrics(ROOT_DIR, FILE_NAME)
            print("** removeLyrics function done **")
            addLyrics(ROOT_DIR, FILE_NAME)
            print("** addLyrics function done **")
        elif(ifLyrics(ROOT_DIR, FILE_NAME) == 1):
            print("***ALL OK ***")

"""-------------------------------------------------Parameter: TIT2--------------------------------------------------------------- """
# TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT

# title, album, Lead performer, band, performer sort order, year, content type, lyrics
# tag names: title, album, lead, band, performerSortOrder, year, contentType

# TIT2 is Title of the song.

class EditMetadata:
    
    def __init__(self):
        
    def ifTag(self,root_dir, fileName,tag):
        filePath = os.path.join(root_dir, fileName)
        if tag=="title":
            title=getTitleMetadata(filePath)
            if (len(title)==0):
                print (0)
                return 0
            else:
                print (1)
                return 1
        elif tag=="album":
            album=getAlbumMetadata(filePath)
            if(len(album)==0):
                print (0)
                return 0
            else:
                print (1)
                return 1
        elif tag=="lead":
            lead=getLeadMetadata(filePath)
            if (len(lead)):
                print (0)
                return 0
            else:
                print (1)
                return 1
        elif tag=="band":
            band=getBandMetadata(filePath)
            if (len(band)):
                print (0)
                return 0
            else:
                print (1)
                return 1
        elif tag=="performerSortOrder":
            pso=getPSOMetadata(filePath)
            if (len(pso)):
                print(0)
                return 0
            else:
                print (1)
                return 1
        elif tag=="year":
            year=getYearMetadata(filePath)
            if (len(year)):
                print (0)
                return 0
            else:
                print (1)
                return 1
        elif tag=="contentType":
            cType=getCTypeMetadata(filePath)
            if (len(cType)):
                print (0)
                return 0
            else:
                print (1)
                return 1
        else:
            print ("error")

    # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT
    # tag names: title, album, lead, band, performerSortOrder, year, contentType
        
    # remove lyrics form corresponding ID3 tag from file
    def removeTag(self,root_dir, file_name,tag):
        filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)
        if tag=="title":
            audio.delall('TIT2')
            audio.add(TIT2(encoding=3, text=u" "))
            
        elif tag=="album":
            audio.delall('TALB')
            audio.add(TALB(encoding=3, text=u" "))
            
        elif tag=="lead":
            audio.delall('TPE1')
            audio.add(TPE1(encoding=3, text=u" "))
            
        elif tag=="band":
            audio.delall('TPE2')
            audio.add(TPE2(encoding=3, text=u" "))
            
        elif tag=="performerSortOrder":
            audio.delall('TSOP')
            audio.add(TSOP(encoding=3, text=u" "))
            
        elif tag=="year":
            audio.delall('TDRC')
            audio.add(TDRC(encoding=3, text=u" "))
            
        elif tag=="contentType":
            audio.delall('TCON')
            audio.add(TCON(encoding=3, text=u" "))
            
        else:
            print ("error: tag unidentified")
            return "error"
        return audio.save()


    # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT
    # tag names: title, album, lead, band, performerSortOrder, year, contentType

    # fetch lyrics and add to corresponding ID3 tag from file
    def addTag(self,root_dir, file_name,songMetadata,tag):
        filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)

        if tag=="title":
            audio.add(TIT2(encoding=3, text=fetchTag(songMetadata,tag)))
        elif tag=="album":
            audio.add(TALB(encoding=3, text=fetchTag(songMetadata,tag)))
        elif tag=="lead":
            audio.add(TPE1(encoding=3, text=fetchTag(songMetadata,tag)))
        elif tag=="band":
            audio.add(TPE2(encoding=3, text=fetchTag(songMetadata,tag)))
        elif tag=="performerSortOrder":
            audio.add(TSOP(encoding=3, text=fetchTag(songMetadata,tag)))
        elif tag=="year":
            audio.add(TDRC(encoding=3, text=fetchTag(songMetadata,tag)))
        elif tag=="contentType":
            audio.add(TCON(encoding=3, text=fetchTag(songMetadata,tag)))
        else:
            print ("error: tag not recognised")
            return "error"
        
        return audio.save()
    # fetches lyrics from lololyrics.com
    # def fetchLyrics(self,file_path):
    #     artist = getArtistMetadata(file_path)
    #     title = getTitleMetadata(file_path)
    #     return(loloLyrics.getLyrics(artist, title))

    # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT
    # tag names: title, album, lead, band, performerSortOrder, year, contentType


    def fetchTag(self,songMetadata,tag):
        if tag=="title":
            return songMetadata["TIT2"]
        elif tag=="album":
            return songMetadata["TALB"]
        elif tag=="lead":
            return songMetadata["TPE1"]
        elif tag=="band":
            return songMetadata["TPE2"]
        elif tag=="performerSortOrder":
            return songMetadata["TSOP"]
        elif tag=="year":
            return songMetadata["TDRC"]
        elif tag=="contentType":
            return songMetadata["TCON"]
        else:
            print ("error: tag unidentified")
            return "error"

        
#   songMetadata is an object of ManageMetaData  class
    def writeTag(self,ROOT_DIR,FILE_NAME,songMetadata,tag):
        
        # deferencing the songMetadata object and storing it in a dictionary

        metaDict={}
        
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


        metaDict["TPE1"]=songMetadata.artistTPE1
        metaDict["TPE2"]=songMetadata.artistTPE2
        metaDict["TIT2"]=songMetadata.titleTIT2
        metaDict["TALB"]=songMetadata.albumTALB
        metaDict["TSOP"]=songMetadata.artistTSOP
        metaDict["TDRC"]=songMetadata.recDateTDRC
        metaDict["TCON"]=songMetadata.genreTCON

        if(ifTag(ROOT_DIR, FILE_NAME,tag) == 0):
            removeTag(ROOT_DIR, FILE_NAME,tag)
            print("** removeTag function done **")
            addTag(ROOT_DIR, FILE_NAME,metaDict,tag)
            print("** addTag function done **")
        elif(ifTag(ROOT_DIR, FILE_NAME,tag) == 1):
            print("***ALL OK ***")
