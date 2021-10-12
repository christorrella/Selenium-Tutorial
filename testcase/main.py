import unittest
from selenium import webdriver

# the file page.py
import page

class PythonOrgSearch(unittest.TestCase):

    # Will run this before every test func "test_.*"
    def setUp(self):
        self.driver = webdriver.Chrome("./driver/chromedriver")
        self.driver.get("http://www.python.org")

    def test_title(self):
        mainPage = page.MainPage(self.driver)
        assert mainPage.is_title_matches()

    def test_search_python (self):

        # Create mainpage object
        mainPage = page.MainPage(self.driver)
        # Check title is OK
        assert mainPage.is_title_matches()
        # Set the mainpage serach text element to have value pycon
        mainPage.search_text_element = "pycon"
        # Click the go button
        mainPage.click_go_button()

        # Create search results page object
        search_result_page = page.SearchResultPage(self.driver)
        # Check if results were found
        assert search_result_page.is_results_found()

    # Because this method starts with "test", it will automatically be run when we run the unit test
    def test_example(self):
        print("Test")
        assert True

    # method doesn't start with "test", won't auto run
    def not_a_test(self):
        print("this won't print")

    # Will run after this test case has finished
    def teardown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
