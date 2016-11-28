import sys
import unittest
import PyQt5
from PyQt5.QtWidgets import QApplication
from PyQt5.QtTest import QTest
from PyQt5.QtCore import Qt
sys.path.append('../recommend/')
from main import MainWindow as mnw
app = QtWidgets.QApplication(sys.argv)

class Test1_extraSetup(unittest.TestCase):
    '''test recommend GUI'''
    def setUp(self):
        '''testing initializes'''
        global obj
        obj = mnw() # 'obj' an object of class 'mnw'

    def test_browseHandler(self):
        self.assertTrue(obj.browseHandler(self))
        #self.assertEqual(editMet)

    def tearDown(self):
        del globals()['obj']
