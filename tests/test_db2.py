import os
import sys
import unittest

sys.path.append('../recommend/LocalStorage/')
from ManageLocalStorageModule import ManageLocalStorage as mls

class Test1(unittest.TestCase):
    ## initiate instance of mls object
    obj = mls('someConnection123')
        
    ## test for build
    def test010_build(self):
        self.assertEqual(self.obj.build(), True)

# Test for 'query'
class Test2(unittest.TestCase):
    def setUp(self):
        self.obj = Test1.obj
    ## test for query
    def test020_query(self):
        self.assertNotEqual(self.obj.query(), "Query failed")
    def tearDown(self):
        del self.obj

# Test for 'dump'
class Test3(unittest.TestCase):
    def setUp(self):
        self.obj = Test1.obj
    
    def test030_dump(self):
        self.assertEqual(self.obj.dump(), True)
    ## tearDown
    def tearDown(self):
        print("tearing down...")
        del self.obj
        del Test1.obj
        os.remove("PRLocalStorage.sqlite3")

if __name__ == "__main__":
    unittest.main()






# class Test01_build(unittest.TestCase):
    # def setUp(self):
    #     ## intializing instance of mls
    #     print("setting up.....................................")
    #     self.obj = mls('something') # connectionName passed

    # def test_build(self):
    #     print('testing.........................................')
    #     self.assertEqual(self.obj.build(), True)
    
    # def test_query(self):
    #     print("testing query........................................")
    #     self.assertNotEqual(mls.query(mls), 'Query failed')

    # def tearDown(self):
    #     print("tearing down........................................")
    #     del self.obj
    #     os.remove("PRLocalStorage.sqlite3")

    
    # def test_connect(self):
    #         print("testing connect........................................")
    #         self.assertEqual(mls.connect(mls), True)
    
    # def test_disconnect(self):
    #     print("testing disconnect.........................................")
    #     self.assertEqual(mls.disconnect(mls), True)

    # def test_dump(self):
    #     mls.isConnected = True
    #     print('testing........................................')
    #     self.assertEqual(mls.dump(mls), True)

# Test for 'build'