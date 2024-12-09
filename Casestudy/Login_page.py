import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys


class Add_to_cart():

    def __init__(self, driver):
        self.driver = driver

    _vitamin_btn = "//button[normalize-space()='Vitamins']"
    _veganChocolate_btn = "//button[normalize-space()='Vegan Chocolate']"
    _vitaminC_btn = "//div[normalize-space()='Vitamin C']"
    _ProductVC_btn = "//a[1]//div[1]//div[3]//div[2]//button[1]"
    _ProductVG_btn = "//a[1]//div[1]//div[3]//div[2]//button[1]"

    def getVitaminandSupplements(self):
        partial_link = "Vitamins"
        self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link).click()

    def getVitamins(self):
        return self.driver.find_element(By.XPATH, self._vitamin_btn)

    def getVitaminC(self):
        return self.driver.find_element(By.XPATH, self._vitaminC_btn)

    def AddvitaminC(self):
        return self.driver.find_element(By.XPATH, self._ProductVC_btn)

    def Clickvitmins(self):
        self.getVitamins().click()

    def clickvitaminC(self):
        self.getVitaminC().click()

    def clickAdditems(self):
        self.AddvitaminC().click()

    def getVegan(self):
        partial_link = "Vegan"
        self.driver.find_element(By.PARTIAL_LINK_TEXT, partial_link).click()

    def getVeganChocolate(self):
        return self.driver.find_element(By.XPATH, self._veganChocolate_btn)

    def Addveganchoc(self):
        return not self.driver(By.XPATH, self._ProductVG_btn)

    def clickvgchoc(self):
        self.getVeganChocolate().click()

    def clickAddvg(self):
        self.Addveganchoc().click()

    def ClickMyB(self):
        self.driver.find_element(By.CSS_SELECTOR, ".HeaderLinkIcon-module_button__C7r3R svg").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Checkout']").click()
        time.sleep(3)

    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()
        self.driver.save_screenshot(".//clickLoginButton.png")
        self.get()
        self.getVitaminandSupplements()
        self.Clickvitamins()
        self.clickvitaminC()
        self.AddItemsVitaminC()
        self.driver.save_screenshot(".//AddItemsVitaminC.png")
        self.ClickHm()
        self.getVegan()
        self.clickvgchoc()
        self.AddVeganItems()
        self.driver.save_screenshot(".//AddVeganItems.png")
        self.ClickMyB()
        self.driver.save_screenshot(".//ClickMyB.png")

