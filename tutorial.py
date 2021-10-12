# Webdriver is used for interasction between Selenium and Chrome
from selenium import webdriver

from selenium.webdriver.common.action_chains import ActionChains

# Specify path for the Chrome webdriver
PATH = "./driver/chromedriver"

# Instantiate a Chrome browser with path to driver
driver = webdriver.Chrome(PATH)

# Open the Chrome browser with the http target of Google
driver.get("https://orteil.dashnet.org/cookieclicker/")

# Implicit wait, exactly 5 seconds (diff from explicit wait)
driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id("cookies")

# get upgrades list from most expensive item to least
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]

# Set up ActionChains obj that will act on the Chrome driver
# Action Chains contain a queue of steps that can be carried out as a set
# Perform those actions any time with .perform func
actions = ActionChains(driver)
actions.click(cookie)

# do this 5,000 times
for i in range(5000):
    actions.perform()
    count = int(cookie_count.text.split(" ")[0])
    print(count)
    for item in items:
        value = int(item.text)

        # if we have enough cookies, buy an upgrade

        if value <= count:
            upgrade_actions = ActionChains(driver)
            upgrade_actions.move_to_element(item)
            upgrade_actions.click()
            upgrade_actions.perform()
