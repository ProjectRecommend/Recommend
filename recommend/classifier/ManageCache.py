class ManageCache(object):

    def __init__(self):
        # don init stuff
        pass

    def ReadCache(self, songID):
        return {}

    def WriteCache(self, PredictedSongDict, songID):
        return False

    def InvalidateCache(self):
        return False

    def DumpCache(self):
        return False

    def DeleteCache(self, songID):
        return False
