from metadataMod import tags 

class ManageMetaData(object):
    def __init__(self):
        # don init stuff
        self.SongMetaData = None
        # impliment member var stuff

    def ReadMetaData(self, SongPath):
        #this function simply trys to get the metadata from the song and return it if it is found.
        
        return {}

    def WriteMetaData(self, SongPath, SongMetaData):
        # this function writes metadata in the song
        return False

    def FetchMetaDataFromMusicBrainz(self, SongMetaData):
        return {}

    def EditMetaData(self, SongPath):
        return False

    def getSongMetaData(self):
        return {}

    def setSongMetaData(self, SongMetaData):
        return False
