from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from utils import *
from skyscanner import *

class SkyScannerTest(object):
    
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.skyscanner.pl"
        #self.verificationErrors = []
        #self.accept_next_alert = True
    
    def test(self, data):
        dep, dest, std, sta = data
        driver = self.driver
        driver.get(self.base_url)
        search = Search(driver)
        search.set_dep(dep)
        search.set_dest(dest)
        search.set_std(std)
        search.set_sta(sta)
        results = search.search()
        return results.get_results()
    
    def tearDown(self):
        self.driver.quit()
        #self.assertEqual([], self.verificationErrors)

'''
import unittest
import numpy
import funcs

# get references to functions
# only the functions and if their names start with "matrixOp"
functions_to_test = [v for k,v in funcs.__dict__ if v.func_name.startswith('matrixOp')]

# suplly an optional setup function
def setUp(self):
    self.matrix1 = numpy.ones((5,10))
    self.matrix2 = numpy.identity(5)

# create tests from functions directly and store those TestCases in a TestSuite
test_suite = unittest.TestSuite([unittest.FunctionTestCase(f, setUp=setUp) for f in functions_to_test])


if __name__ == "__main__":
unittest.main()
    '''
