from selenium import webdriver
import time

# Specify path for the Chrome webdriver
PATH = "./driver/chromedriver"

# Instantiate a Chrome browser with path to driver
driver = webdriver.Chrome(PATH)

# Open the Chrome browser with the http target of Google
driver.get("http://www.google.com")

# Close the Google tab
driver.close()
