import unittest#file name starts with test_ or ends with _test
import self
from selenium import webdriver

class Test(unittest.TestCase):
    def testName(self):
        driver = webdriver.Chrome()
        driver.get("https://www.google.co.in/")
        TitleOfBrowser = driver.title
        self.assertTrue(TitleOfBrowser == "Google")
        #self.assertFalse(TitleOfBrowser == "Google123")

if __name__ == "__main_":
    unittest.main()