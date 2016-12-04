from selenium.webdriver.common.by import By 
import utilities.custom_logger as cl
import logging
import unittest
from base.basepage import BasePage


class AlertPopupPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    _alert_button = "alertbtn"

    # Selectors
    def getAlertButton(self):
        return self.driver.find_element(By.ID, self._alert_button)

    # Actions
    def clickOnAlertButton(self):
        self.getAlertButton().click()

    # Methods
    def acceptJavaScriptAlertPopup(self):
        self.clickOnAlertButton()
        alertPopup = self.driver.switch_to.alert       # javascript function provided by webdriver that allows you to interact with popup
        alertPopup.accept()                            # accept() method on popup clicks its "ok" button and makes popup disappear
        return self