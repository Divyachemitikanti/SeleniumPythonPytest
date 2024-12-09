from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import unittest
from Login_page import Add_to_cart
import time

from Casestudy.Login_page import Add_to_cart
from POM.Login_Page import LoginPage


class LoginTests(unittest.TestCase):
    def test_validateLogin(self):
        baseUrl = "https://auth.hollandandbarrett.com/u/login"
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://auth.hollandandbarrett.com/")
        time.sleep(5)

    def Add_to_cart(self,email,password):
        lp = LoginPage(driver)
        lp.login("divyach74@gmail.com", "Divya@516")










