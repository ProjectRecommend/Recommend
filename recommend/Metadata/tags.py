'''
this module contains functions that extracts metadata from
mp3 file and returns a python list of UniCode Characters
NOTE : Windows Does't support unicode in powershell and console by default

run `chcp 65001` if you getting erros releted to unicode in windows

'''

from mutagen.id3 import ID3
from bs4 import UnicodeDammit

class getTags(object):
    
    def __init__(self,mp3file):
        self.audio=ID3(mp3file)
        self.tags=self.audio.items()

    def getLyricsMetadata(self):
        metaText=""
        for tag in self.tags:
            if (tag[0] == 'USLT::eng'):
                metaText=(str(tag[1]).encode(encoding='utf_8'))
        return self.metaTextToUnicode(metaText)


    def getArtistMetadata(self):
        metaText=""
        for tag in self.tags:
            if (tag[0] == 'TPE1'):
                metaText=(str(tag[1]).encode(encoding='utf_8'))

        return self.metaTextToUnicode(metaText)


    def getTitleMetadata(self):
        metaText=""
        for tag in self.tags:
            if (tag[0] == 'TIT2'):
                metaText=(str(tag[1]).encode(encoding='utf_8'))
        print ("getTitleMetadata :")
        print (metaText)
        return self.metaTextToUnicode(metaText)

    # from tags import (getLyricsMetadata, getArtistMetadata, getTitleMetadata, getAlbumMetadata, getLeadMetadata, getBandMetadata, getPSOMetadata, getYearMetadata, getCTypeMetadata)
    # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT

    # title, album, Lead performer, band, performer sort order, year, content type, lyrics
    # tag names: title, album, lead, band, performerSortOrder, year, contentType


    def getAlbumMetadata(self):
        metaText=""
        for tag in self.tags:
            if (tag[0] == 'TALB'):
                metaText=(str(tag[1]).encode(encoding='utf_8'))

        return self.metaTextToUnicode(metaText)


    def getLeadMetadata(self):
        metaText=""
        for tag in self.tags:
            if (tag[0] == 'TPE1'):
                metaText=(str(tag[1]).encode(encoding='utf_8'))

        return self.metaTextToUnicode(metaText)


    def getBandMetadata(self):
        metaText=""
        for tag in self.tags:
            if (tag[0] == 'TPE2'):
                metaText=(str(tag[1]).encode(encoding='utf_8'))

        return self.metaTextToUnicode(metaText)


    def getPSOMetadata(self):
        metaText=""
        for tag in self.tags:
            if (tag[0] == 'TSOP'):
                metaText=(str(tag[1]).encode(encoding='utf_8'))

        return self.metaTextToUnicode(metaText)


    def getYearMetadata(self):
        metaText=""
        for tag in self.tags:
            if (tag[0] == 'TDRC'):
                metaText=(str(tag[1]).encode(encoding='utf_8'))

        return self.metaTextToUnicode(metaText)


    def getCTypeMetadata(self):
        metaText=""
        for tag in self.tags:
            if (tag[0] == 'TCON'):
                metaText=(str(tag[1]).encode(encoding='utf_8'))

        return self.metaTextToUnicode(metaText)


    # returns a string converted from metaText to Unicode
    def metaTextToUnicode(self,metaText):
        # print(metaText)
        final = []
        uniText = []
        split = metaText.split()

        # metaText is now a string and we are first splitting the string for getting it into the list split, using that list
        # we are appending each string to final. 

        for text in split:
            final.append(text)

        # uniText is finally a list that contains all the elements in normal text not unicode.

        for text in final:
            dammit = UnicodeDammit(text)
            uniText.append(dammit.unicode_markup)

        # final_text is a string that shows metaText in normal form.

        final_text = ' '.join(uniText)
        # print('*metaTextToUnicode DONE*')
        return final_text
