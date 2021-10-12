# Classes for each web page that we visit

from locator import *
from element import BasePageElement

class SearchTextElement(BasePageElement):
    locator = "q"

class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

# Inherit the methods from BasePage for MainPage
class MainPage(BasePage):

    search_text_element = SearchTextElement()

    # Check to make sure title of webpage matches what we need it to be
    def is_title_matches(self):
        return "Python" in self.driver.title

    def click_go_button(self):
        # Find elements that is denoted by the locator that is in locators.py for mainpage
        # Use splat/unpack to use tuple as args
        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()

class SearchResultPage(BasePage):

    # if "no results found" is in the page source, return false, else true
    def is_results_found(self):
        return "No results found." not in self.driver.page_source
