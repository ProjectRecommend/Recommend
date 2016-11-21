# SongMetadata Object, it is used to pass data(ID3 data) around
# see this : https://en.wikipedia.org/wiki/ID3
# for more info about ID3 tags


class SongMetadata(object):
    
    # TIT2,TALB,TPE1,TPE2,TSOP,TDRC,TCON,USLT
    # tag names: title, album, lead, band, performerSortOrder, year, contentType/genre

    def __init__(self):
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
