import os
import sys
import unittest

sys.path.append('../recommend/')
from LocalStorage.ManageLocalStorageModule import ManageLocalStorage as mls
from LocalStorage.AccessLocalStorageModule import AccessLocalStorage as als

## test for 'build'
class Test10(unittest.TestCase):
    ## initiate instance of mls object
    #obj_mls = mls('someConnection123')

    def setUp(self):
        global obj_mls 
        obj_mls = mls('someConnect123')
    def test_build(self):
        print("/t/ttest010")
        self.assertEqual(obj_mls.build(), True)

# Test for 'query'
class Test20(unittest.TestCase):
    def setUp(self):
        #self.obj_mls = Test10.obj_mls
        pass
    def test_query(self):
        print("/t/ttest020")
        self.assertNotEqual(obj_mls.query(), "Query failed")
    def tearDown(self):
        pass
        #del self.obj

# Test for 'write'
class Test30(unittest.TestCase):
    def setUp(self):
        print("setting up")
        global obj_als
        obj_als = als('someConnect123')
        global SongPath
        SongPath = "saang.mp3"
        #obj_als = als('someConnection123')
    def test_write(self):
        print("\n\t\tttest030")
        print("testing for write.....")
        self.assertEqual(obj_als.write(SongPath), True)

# Test for 'read'
class Test40(unittest.TestCase):
    def setUp(self):
        print("setting up for read...")
    def test_read(self):
        print("\n\t\ttest040")
        print("testing read function...")
        self.assertNotEqual(obj_als.read(SongPath), False)
    def tearDown(self):
        print("tearing down for read...")
        pass

# Test for 'update'
class Test41(unittest.TestCase):
    def setUp(self):
        pass
    def test_update(self):
        print("\n\ttest41...")
        self.assertEqual(obj_als.update(SongPath), True)
    def tearDown(self):
        del globals()['SongPath']


# Test for 'delete'
class Test42(unittest.TestCase):
    def setUp(self):
        print("setting up for delete...")
        self.SongID = 100
    def test_delete(self):
        print("\ntest042")
        print("testing delete function...")
        self.assertEqual(obj_als.delete(self.SongID), True)
    def tearDown(self):
        del self.SongID

# Test for 'dump'
class Test50(unittest.TestCase):
    def setUp(self):
        pass
        # self.obj_mls = obj
    def test_dump(self):
        print("\n\t\ttest050")
        self.assertEqual(obj_mls.dump(), True)
    def tearDown(self):
        print("tearing down...")
        del globals()['obj_mls']
        del globals()['obj_als']
        os.remove("PRLocalStorage.sqlite3")




if __name__ == "__main__":
    unittest.main()