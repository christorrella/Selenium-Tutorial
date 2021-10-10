# Webdriver is used for interasction between Selenium and Chrome
from selenium import webdriver

# Keys are used an inputs into the page from an automated keyboard
from selenium.webdriver.common.keys import Keys
import time

# Explicit waits
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Specify path for the Chrome webdriver
PATH = "./driver/chromedriver"

# Instantiate a Chrome browser with path to driver
driver = webdriver.Chrome(PATH)

# Open the Chrome browser with the http target of Google
driver.get("https://www.techwithtim.net/")


# Click three links on pages by link text and ID, and then go back in browser to root website
# Using explicit waits
try:
    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Python Programming"))
    )
    link.click()

    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    link.click()

    link = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    link.click()

    driver.back()
    driver.back()
    driver.back()

except:
    driver.quit()
