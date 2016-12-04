from selenium.webdriver.common.by import By 
import utilities.custom_logger as cl
import logging
import unittest
from base.basepage import BasePage


class ConfirmPopupPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    _confirm_button = "confirmbtn"

    # Selectors
    def getAlertButton(self):
        return self.driver.find_element(By.ID, self._confirm_button)

    # Actions
    def clickOnConfirmButton(self):
        self.getAlertButton().click()

    # Methods
    def acceptJavaScriptConfirmPopup(self):
        self.clickOnAlertButton()
        confirmPopup = self.driver.switch_to.alert       # javascript function provided by webdriver that allows you to interact with popup
        confirmPopup.accept()                            # accept() method on popup clicks its "ok" button and makes popup disappear
        return self

    def dismissJavaScriptConfirmPopup(self):
        self.clickOnConfirmButton
        confirmPopup = self.driver.switch_to.alert 
        confirmPopup.dismiss()                         # accept() method on popup clicks its "cancel" button and makes popup disappear
        return self 