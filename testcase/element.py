from selenium.webdriver.support.ui import WebDriverWait

class BasePageElement(object):

    # Any time we want to set a value on the page, i.e. a form value,
    def __set__(self, obj, value):

        #obtain the objects driver,
        driver = obj.driver

        #Wait up to 100 seconds until this element is present on the page
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))

        # clear the present value and set it to the vlaue from func params
        driver.find_element_by_name(self.locator).clear()
        driver.find_element_by_name(self.locator).send_keys(value)

    # Any time we want to get a value on the page, i.e. a form value,
    def __get__(self, obj, owner):

        #obtain the objects driver,
        driver = obj.driver

        #Wait up to 100 seconds until this element is present on the page
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element_by_name(self.locator))

        # get that element and return it
        element = driver.find_element_by_name(self.locator)
        return element.get_attribute("value")
