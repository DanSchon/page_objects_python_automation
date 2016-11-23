from selenium.webdriver.common.by import By 
import utilities.custom_logger as cl
import logging
import unittest
from base.basepage import BasePage

from selenium.webdriver import ActionChains
import time

class DragAndDropPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    _slider_handle = "//div[@id='slider']//span"
    _success_message = "//div[contains(@class,'flash-message') and contains(text(),'Slider handle moved successfully')]"


    # Selectors
    def sliderHandle(self):
        return self.driver.find_element(By.XPATH, self._slider_handle)

    # Actions 
    def moveSliderHandleToTheMiddleOfTheSlideBar(self):
        actions = ActionChains(self.driver)
        actions.drag_and_drop_by_offset(element, 100, 0).perform()
        self.log.info("Moved slider handle to middle of slide bar")
        time.sleep(2)
        return self

    # Assertions    
    def verifyUserMovedSliderHandleSuccessfully(self):
        successMessageElement = self.waitForElement(self._success_message, locatorType="xpath")
        result = successMessageElement.is_displayed()
        self.verify(result, "Passed", "Movement of Slider Handle Was Not Successful")