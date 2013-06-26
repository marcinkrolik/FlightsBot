from selenium import webdriver
#from selenium.webdriver.common.by import By
#from selenium.webdriver.support.ui import Select
#from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from utils import *

class Search(object):
    
    # static tuples representing page items as "how" and "what"
    DEPARTURE = ("id", "sc_fromPlace")
    DESTINATION = ("id", "sc_toPlace")
    CALENDAR_NEXT_MONTH = ("css_selector", "a.ss_calendar_next")
    STD = ("id", "sc_departDate")
    STA = ("id", "sc_returnDate")
    SEARCH_BUTTON = ("id", "sc_search")
    
    def __init__(self, driver):
        # during init just wait for search button to be enabled 
        self.driver = driver
        WebDriverWait(self.driver, 10).until(lambda driver: find(driver, self.SEARCH_BUTTON).is_enabled())
    
    def set_dep(self, dep):
        # clear departure and send string
        find(self.driver, self.DEPARTURE).clear()
        find(self.driver, self.DEPARTURE).send_keys(dep)
    
    def set_dest(self, dest):
        # clear destination and send string
        find(self.driver, self.DESTINATION).clear()
        find(self.driver, self.DESTINATION).send_keys(dest)
    
    def set_std(self, std):
        # clear time of departure and send string
        find(self.driver, self.STD).clear()
        find(self.driver, self.STD).send_keys(std)
    
    def set_sta(self, sta):
        # clear time of destination and send string
        find(self.driver, self.STA).clear()
        find(self.driver, self.STA).send_keys(sta)
    
    def search(self):
        # click on search button, take all handlers to pages and close all but default one
        find(self.driver, self.SEARCH_BUTTON).click()
        for h in self.driver.window_handles[1:]:
            self.driver.switch_to_window(h)
            self.driver.close()
        self.driver.switch_to_window(self.driver.window_handles[0])
        return Results(self.driver)

class Results(object):
    
    SPAN = "span.price"
    ROW = ("xpaths", "//*[@class='px PLN']")
    
    def __init__(self, driver):
        # during init just wait the best price to be visible 
        self.driver = driver
        WebDriverWait(self.driver, 60).until(lambda driver: driver.find_element_by_css_selector(self.SPAN).is_enabled())
    
    def get_results(self):
        how, what = self.ROW
        prices = [element.text[:-2].replace(' ', '') for element in find(self.driver, self.ROW)]
        return prices
    
        