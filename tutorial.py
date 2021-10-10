# Webdriver is used for interasction between Selenium and Chrome
from selenium import webdriver

# Keys are used an inputs into the page from an automated keyboard
from selenium.webdriver.common.keys import Keys
import time

# Excplicit Waits, see 5.1 from https://selenium-python.readthedocs.io/waits.html
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Specify path for the Chrome webdriver
PATH = "./driver/chromedriver"

# Instantiate a Chrome browser with path to driver
driver = webdriver.Chrome(PATH)

# Open the Chrome browser with the http target of Google
driver.get("https://www.techwithtim.net/")

print(driver.title)

# find first element with this HTML name
search = driver.find_element_by_name("s")
# send keys to that element
search.send_keys("test")
# hit return to search the website
search.send_keys(Keys.RETURN)

# Explicitly wait up to 10 seconds for the "main" id to show up in the DOM
try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "main"))
    )
    # once we have "main", find all of the articles by tag name
    articles = main.find_elements_by_tag_name("article")
    # for each of those articles, print the text within
    for article in articles:
        header = article.find_element_by_class_name("entry-summary")
        print(header.text)


    # wait and then close
    time.sleep(5)
    driver.quit()
finally:
    driver.quit()
