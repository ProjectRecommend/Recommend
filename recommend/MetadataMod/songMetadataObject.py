# SongMetadata Object, it is used to pass data(ID3 data) around
# see this : https://en.wikipedia.org/wiki/ID3
# for more info about ID3 tags


class SongMetadata(object):
    def __init__(self):
        self.artistNameTPE1 = None
        self.artistNameTPE2 = None
        self.albumNameTALB = None
        self.artistNameTSOP = None
        self.lyricsUSLT = None
        self.dateAndYearOfRecordingTDRC = None
        self.dateAndYearOfReleaseTDOR = None
        self.publisherTPUB = None
        self.titleTIT2 = None
        self.genreTCON = None
