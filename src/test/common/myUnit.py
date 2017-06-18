# coding:utf-8
import unittest
from driver import remote


class MyTest(unittest.TestCase):
    def setUp(self):
        print "------------------setUp-------------------"
        self.driver = remote()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        print "-----------------tearDown-----------------"
        self.driver.quit()
