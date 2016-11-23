from selenium.webdriver.common.by import By 
import utilities.custom_logger as cl
import logging
import unittest
from base.basepage import BasePage

from selenium.webdriver import ActionChains
import time

class MouseHoveringPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    _element_to_hover_mouse_over = "mousehover"
    _element_that_appears_in_dropdown_after_hovering = "//div[@class='mouse-hover-content']//a[text()='Log Out']"
    _logout_message = "//div[contains(@class,'flash-message') and contains(text(),'Logged Out Successfully')]"


    # Selectors
    def dropdown(self):
        return self.driver.find_element(By.ID, self._element_to_hover_mouse_over)
    def elementThatAppearsInDropdownAfterHovering(self):
        return self.driver.find_element(By.XPATH, self._element_that_appears_in_dropdown_after_hovering)
    

    # Actions
    def mouseHoverOverDropdown(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.dropdown()).perform()
        self.log.info("Mouse Hovered on dropdown element")
        time.sleep(2)
        return self
    def clickElementThatAppearsInDropdownAfterHovering(self):
        actions = ActionChains(self.driver)
        actions.move_to_element(self.elementThatAppearsInDropdownAfterHovering()).click().perform()
        self.log.info("Item in Dropdown Clicked")
        time.sleep(2)
        return self

    # Methods
    def hoverMouseOverDropdownAndClickLogoutElementFromDropdownList(self):
        self.mouseHoverOverDropdown()
        self.clickElementThatAppearsInDropdownAfterHovering()
        return self

    # Assertions    
    def verifyUserLoggedOutSuccessfully(self):
        LogoutMessageElement = self.waitForElement(self._logout_message, locatorType="class")
        result = LogoutMessageElement.is_displayed()
        self.verify(result, "Passed", "Log Out Was Not Successful")
