import os
import sys
import unittest

sys.path.append('../recommend/')
from Metadata.ManageMetaDataModule import ManageMetaData as mmd

# Test for 'ReadMetaData'
class Test10_ReadMetaData(unittest.TestCase):
    def setUp(self):
        global obj
        obj = mmd()
        global SongPath
        SongPath = 'sample_song.mp3'
    def test(self):
        global songMetaData
        songMetaData = obj.ReadMetaData(SongPath)
        self.assertEqual(isinstance(songMetaData, dict), True)

# Test for 'WriteMetaData'
class Test20_WriteMetaData(unittest.TestCase):
    def setUp(self):
        pass
    def test(self):
        self.assertEqual(obj.WriteMetaData(songMetaData, SongPath), True)
    def tearDown(self):
        del globals()['obj']
        del globals()['SongPath']
        del globals()['songMetaData']

if __name__ == '__main__':
    unittest.main()