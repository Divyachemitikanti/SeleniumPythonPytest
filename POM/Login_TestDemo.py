import time
from unittest import TestCase

from selenium import webdriver
import unittest

from POM.Login_Page import LoginPage


class LoginTests(unittest.TestCase):

    def test_validateLogin(self):
        baseUrl = "https://auth.hollandandbarrett.com/u/login"
        driver = webdriver.Chrome()
        driver.get("https://auth.hollandandbarrett.com/u/login")

        driver.maximize_window()
        time.sleep(5)

        lp = LoginPage(driver)
        lp.login( "divyach74@gmail.com", "Divya@516")

        actual_title = driver.title
        expect_title = "Sign in - to your account, for the best experience"

        if actual_title == expect_title:
            print("Login is succesful ...... well done python")

        else:
            print("Login Unsuccesful ..... very good my boy")




