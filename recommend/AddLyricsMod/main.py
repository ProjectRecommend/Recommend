# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 16:17:21 2016
"""
import os

#this module provides a portable way of using operating system dependent functionality, file manipulations for example.

# import loloLyrics module
import loloLyrics

# metadata module
from tags import (getLyricsMetadata, getArtistMetadata, getTitleMetadata, getAlbumMetadata)

from mutagen.id3 import USLT
from mutagen.id3 import ID3

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

# TIT2 is Title of the song.

class EditTIT2:
    
    def __init__(self):
        
    def ifTitle(self,root_dir, fileName):
        filePath = os.path.join(root_dir, fileName)
        title = getTitleMetadata(filePath) # list of elements    
        # Assuming that a song can't have lyrics lesses than 15 words
        if(len(title)==0):
            print(0)
            return(0)
        else: 
            print(1)
            return(1)
        
    # remove lyrics form corresponding ID3 tag from file
    def removeTitle(self,root_dir, file_name):
        filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)
        audio.delall('TIT2')
        audio.add(TIT2(encoding=3, text=u" "))
        return audio.save()
        
    # fetch lyrics and add to corresponding ID3 tag from file
    def addTitle(self,root_dir, file_name,songMetadata):
        filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)
        audio.add(TIT2(encoding=3, text=fetchTitle(songMetadata)))
        return audio.save()

    # fetches lyrics from lololyrics.com
    # def fetchLyrics(self,file_path):
    #     artist = getArtistMetadata(file_path)
    #     title = getTitleMetadata(file_path)
    #     return(loloLyrics.getLyrics(artist, title))

    def fetchTitle(self,songMetadata):
        return songMetadata["TIT2"]
        
   
    def writeTitle(self,ROOT_DIR,FILE_NAME,songMetadata):
        if(ifTitle(ROOT_DIR, FILE_NAME) == 0):
            removeTitle(ROOT_DIR, FILE_NAME)
            print("** removeLyrics function done **")
            addTitle(ROOT_DIR, FILE_NAME,songMetadata)
            print("** addLyrics function done **")
        elif(ifTitle(ROOT_DIR, FILE_NAME) == 1):
            print("***ALL OK ***")

""" ------------------------------------------------Parameter: TALB (Album)------------------------------------------------------"""

class EditTALB:
    def __init__(self):

    def ifAlbum(self,root_dir, fileName):
        filePath = os.path.join(root_dir, fileName)
        album = getAlbumMetadata(filePath) # list of elements    
        # Assuming that a song can't have lyrics lesses than 15 words
        if(len(album)==0):
            print(0)
            return(0)
        else: 
            print(1)
            return(1)
        
    # remove lyrics form corresponding ID3 tag from file
    def removeAlbum(self,root_dir, file_name):
        filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)
        audio.delall('TALB')
        audio.add(TIT2(encoding=3, text=u" "))
        return audio.save()
        
    # fetch lyrics and add to corresponding ID3 tag from file
    def addAlbum(self,root_dir, file_name,songMetadata):
        filePath = os.path.join(root_dir, file_name)
        audio = ID3(filePath)
        audio.add(TIT2(encoding=3, text=fetchTitle(songMetadata)))
        return audio.save()

    # fetches lyrics from lololyrics.com
    # def fetchLyrics(self,file_path):
    #     artist = getArtistMetadata(file_path)
    #     title = getTitleMetadata(file_path)
    #     return(loloLyrics.getLyrics(artist, title))

    def fetchTitle(self,songMetadata):
        return songMetadata["TIT2"]
        
   
    def writeTitle(self,ROOT_DIR,FILE_NAME,songMetadata):
        if(ifTitle(ROOT_DIR, FILE_NAME) == 0):
            removeTitle(ROOT_DIR, FILE_NAME)
            print("** removeLyrics function done **")
            addTitle(ROOT_DIR, FILE_NAME,songMetadata)
            print("** addLyrics function done **")
        elif(ifTitle(ROOT_DIR, FILE_NAME) == 1):
            print("***ALL OK ***")
