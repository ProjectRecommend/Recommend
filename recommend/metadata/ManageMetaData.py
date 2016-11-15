class ManageMetaData(object):
    def __init__(self):
        # don init stuff
        self.SongMetaData = None
        # impliment member var stuff

    def ReadMetaData(self, SongPath):
        return {}

    def WriteMetaData(self, SongPath, SongMetaData):
        return False

    def FetchMetaDataFromMusicBrainz(self, SongMetaData):
        return {}

    def EditMetaData(self, SongPath):
        return False

    def getSongMetaData(self):
        return {}

    def setSongMetaData(self, SongMetaData):
        return False
