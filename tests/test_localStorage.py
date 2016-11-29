import os
import sys
import unittest

sys.path.append('../recommend/')
from LocalStorage.ManageLocalStorageModule import ManageLocalStorage as mls
from LocalStorage.AccessLocalStorageModule import AccessLocalStorage as als

# TESTS for ManageLocalStorageModule
# CLASS ManageLocalStorage

# tests for connect() and disconnect() are not written becaues they are not in use

# test for 'build'


class Test10_build(unittest.TestCase):
    def setUp(self):
        global obj_mls
        obj_mls = mls('someConnect123')

    def test_build(self):
        self.assertEqual(obj_mls.build(), True)

# test for 'query'


class Test20_query(unittest.TestCase):
    def setUp(self):
        pass

    def test_query(self):
        self.assertNotEqual(obj_mls.query(), "Query failed")

    def tearDown(self):
        pass

# test for 'dump'


# class Test50_dump(unittest.TestCase):
#     def setUp(self):
#         pass

#     def test_dump(self):
#         self.assertEqual(obj_mls.dump(), True)

#     def tearDown(self):
#         del globals()['obj_mls']
#         del globals()['obj_als']
#         os.remove("PRLocalStorage.sqlite3")


# TESTS for AccessLocalStorageModule
# CLASS AccessLocalStorage

# Test for 'write'

class Test30_write(unittest.TestCase):
    def setUp(self):
        global obj_als
        obj_als = als('someConnect123')
        global SongPath
        SongPath = "sample_song.mp3"

    def test_write(self):
        self.assertEqual(obj_als.write(SongPath), True)

# Test for 'read'


class Test40_read(unittest.TestCase):
    def setUp(self):
        pass

    def test_read(self):
        self.assertNotEqual(obj_als.read(SongPath), False)

    def tearDown(self):
        pass

# Test for 'update'


class Test41_update(unittest.TestCase):
    def setUp(self):
        pass

    def test_update(self):
        self.assertEqual(obj_als.update(SongPath), True)

    def tearDown(self):
        del globals()['SongPath']

# Test for 'delete'


class Test42_delete(unittest.TestCase):
    def setUp(self):
        self.SongID = 100

    def test_delete(self):
        self.assertEqual(obj_als.delete(self.SongID), True)

    def tearDown(self):
        del self.SongID

if __name__ == "__main__":
    unittest.main()
