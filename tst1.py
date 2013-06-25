from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class Tst1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.skyscanner.pl/"
        self.verificationErrors = []
        self.accept_next_alert = true
    
    def test_tst1(self):
        driver = self.driver
        driver.get(self.base_url + "/loty/gdn/mnl/130626/130826/ceny-biletow-lotniczych-z-gda%c5%84sk-do-manila-ninoy-aquino-w-czerwiec-2013-i-sierpien-2013.html")
        driver.find_element_by_css_selector("span.price").click()
        driver.find_element_by_css_selector("li.flexible_view > a > em").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert.text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
