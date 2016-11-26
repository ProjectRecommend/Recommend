import nose2
import nose2.tools
import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlQueryModel
import unittest

sys.path.append('../recommend/LocalStorage/')
from ManageLocalStorageModule import ManageLocalStorage as mls



class Test_build(unittest.TestCase):
    def setUp(self):
        print("setting up.....................................")
        mls.isConnected = False
        mls.connectionName = 'connectionName'
        mls.db = QSqlDatabase.addDatabase('QSQLITE', mls.connectionName)

    def test(self):
        print('testing.........................................')
        self.assertEqual(mls.build(mls), True)

    def tearDown(self):
        print("tearing down.....................................")







class Test_query(unittest.TestCase):
    def setUp(self):
        print("setting up for query........................................")
    def test(self):
        print("testing query........................................")
        self.assertNotEqual(mls.query(mls), 'Query failed')
    def tearDown(self):
        print('tearing down query........................................')



class test_connect(unittest.TestCase):
    def setUp(self):
        print("setting up for connect........................................")
    def test(self):
        print("testing connect........................................")
        self.assertEqual(mls.connect(mls), True)
    def tearDown(self):
        print("tearing down connect........................................")



class test_disconnect(unittest.TestCase):
    def setUp(self):
        print("setting up for connect........................................")
    def test(self):
        print("testing disconnect.........................................")
        self.assertEqual(mls.disconnect(mls), True)
    def tearDown(self):
        print("tearing down.........................................")

class Test_dump(unittest.TestCase):
    def setUp(self):
        print("setting up........................................")
        mls.isConnected = True
    
    def test(self):
        print('testing........................................')
        self.assertEqual(mls.dump(mls), True)

    def tearDown(self):
        print("tearing down........................................")

if __name__ == "__main__":
    nose2.main()

