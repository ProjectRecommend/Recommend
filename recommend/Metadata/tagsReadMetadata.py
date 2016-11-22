'''
this module contains functions that extracts metadata from
mp3 file and returns a python list of UniCode Characters
NOTE : Windows Doesn't support unicode in powershell and console by default

run `chcp 65001` if you getting errors related to unicode in windows
'''
# pip install mutagen
# pip install BeautifulSoup4

from mutagen.id3 import ID3
from bs4 import UnicodeDammit
"""
def __init__(self):
    metaDataDict={}
    metaText = []
"""


def getMetadata(mp3file):

    metaText = []

    audio = ID3(mp3file)
    tags = audio.items()
    """
    print ("type of tags is:")
    print (type(tags))

    print ("tags are:")
    print (tags)
    """
    for tag in tags:
        if (tag[0] == 'USLT::eng'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TALB'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TPE1'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TPE2'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TSOP'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TIT2'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TCON'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TDRC'):
            metaText.append(str(tag[1]).encode(encoding='utf_8'))
    return metaText


def getMetadataDict(mp3file):

    metaDataDict = {}
    audio = ID3(mp3file)
    tags = audio.items()
    """
    print ("type of tags is:")
    print (type(tags))

    print ("tags are:")
    print (tags)
    """
    for tag in tags:
        if (tag[0] == 'USLT::eng'):
            metaDataDict["USLT::eng"] = (str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TALB'):
            metaDataDict["TALB"] = (str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TPE1'):
            metaDataDict["TPE1"] = (str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TPE2'):
            metaDataDict["TPE2"] = (str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TSOP'):
            metaDataDict["TSOP"] = (str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TIT2'):
            metaDataDict["TIT2"] = (str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TCON'):
            metaDataDict["TCON"] = (str(tag[1]).encode(encoding='utf_8'))
        if (tag[0] == 'TDRC'):
            metaDataDict["TDRC"] = (str(tag[1]).encode(encoding='utf_8'))
    return metaDataDict


def metaTextToUnicode(metaText):
    # print(metaText)
    final = []
    uniText = []
    """
    for data in metaText:
        split = data.split()
        for text in split:
            final.append(text)
            """

    for text in metaText:
        dammit = UnicodeDammit(text)
        uniText.append(dammit.unicode_markup)
    return uniText


def metaDataDictToUnicode(metaDataDict):
    final = {}
    uniText = {}
    # metaText not contains all the values as a list
    # dictKeys=metaDataDict.keys()
    # for data in metaDataDict:
    #     split = data.split()
    #     #split is now a list of all the individual words.
    #     for text in split:
    #         final.append(text)

    for text in metaDataDict:
        dammit = UnicodeDammit(metaDataDict[text])
        uniText[text] = dammit.unicode_markup

    return uniText

# print (getMetadataDict("D://Songs(english)//naked//Bony_M_Jingle_Bells.mp3"))
# metaText=getMetadata("D://Songs(english)//naked//Bony_M_Jingle_Bells.mp3")
# print (metaTextToUnicode(metaText))
# metaDataDict=getMetadataDict("D://Songs(english)//naked//Bony_M_Jingle_Bells.mp3")
# print (metaDataDictToUnicode(metaDataDict))
