# Locator file contains all of the ways that we identify specific elements on web pages
# this makes it easy to find the specific html/css/etc elements in this selenium project and change them quickly

from selenium.webdriver.common.by import By

# Define a class that contains all of the locators for the Main Page
class MainPageLocators(object):

    # Definer button by ID, name all caps b/c constant
    GO_BUTTON = (By.ID, "submit")


class SearchResultsPageLocators(object):
    pass
