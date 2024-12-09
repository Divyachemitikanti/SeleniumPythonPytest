import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    #locators
    _email_field = "username"
    _password_field = "password"
    _login_button = "//button[normalize-space()='Sign In']"

    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)

    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._password_field)

    def getLoginButton(self):
        return self.driver.find_element(By.XPATH, self._login_button)

    def enterEmail(self, email):
        self.getEmailField().send_keys(email)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def clickLoginButton(self):
        self.getLoginButton().click()

    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()