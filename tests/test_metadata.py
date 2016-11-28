import os
import sys
import unittest

sys.path.append('../recommend/')
from Metadata.ManageMetaDataModule import ManageMetaData as mmd
import Metadata.tagsReadMetadata as trm

# TEST for ManageMetadataModule
## CLASS MANAGEMETADATA
### Test for 'ReadMetaData'
class Test10_ReadMetaData(unittest.TestCase):
    def setUp(self):
        global obj
        obj = mmd()
        global SongPath
        SongPath = 'sample_song.mp3'
    def test_readMetaData(self):
        global songMetaData
        songMetaData = obj.ReadMetaData(SongPath)
        self.assertEqual(isinstance(songMetaData, dict), True)

### Test for 'WriteMetaData'
class Test20_WriteMetaData(unittest.TestCase):
    def setUp(self):
        pass
    def test_writeMetaData(self):
        self.assertEqual(obj.WriteMetaData(songMetaData, SongPath), True)
    def tearDown(self):
        del globals()['obj']
        del globals()['songMetaData']
        # not deleting global SongPath due to errors in reassignment in Test30

# TESTS for 'tagsReadMetadata'
### TODO test for metaDataDictToUnicode
### Test for getMetadataDict(mp3file)
class Test30_getMetadataDict(unittest.TestCase):
    def setUp(self):
        global val
        val = trm.getMetadataDict(SongPath)
        global OGGSongPath
        #OGGSongPath = 'sample_song.ogg'

    # File is valid
    def test_getMetadataDict_fileValidity(self):
        self.assertEqual(isinstance(val, dict), True)

    # Returned dictionay should not be empty if file is valid
    def test_getMetadataDict_fileNotEmpty(self):
        self.assertEqual((len(val) > 0), True)

    # Returned dictionary should be empty if file is not valid or no file passed
    #def test3(self):
    #   self.assertEqual((len(trm.getMetadataDict(OGGSongPath)) == 0), True)

    def teardown(self):
        del globals()['SongPath']
        #del globals()['OGGSongPath']
        del globals()['val']


# TODO tests for functions in LyricsAndMetaData.py

# Test for metaDataDictToUnicode(metaDataDict)
# class Test40_metaDataDictToUnicode(unittest.TestCase):
#     def setUp(self):
#         global bin_foo_dict
#         foo_dict = {}
#         foo_dict['elB'] = 'B'
#         x = {}
#         x['elAA'] = 'AA'
#         x['elAB'] = 'AB'
#         foo_dict['elA'] = x

#     def test(self):
#         assertEqual(isinstance(metaDataDictToUnicode(foo_dict), unicode), true )
#     def tearDown(self):
#         pass

if __name__ == '__main__':
    unittest.main()
