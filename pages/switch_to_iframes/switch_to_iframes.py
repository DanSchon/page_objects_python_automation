from selenium.webdriver.common.by import By 
import utilities.custom_logger as cl
import logging
import unittest
from base.basepage import BasePage


class SwitchToIframe(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    _iframe_id = "id-iframe"
    _iframe_name = "name-iframe"

    # Actions
    
    def switchToIframeUsingNumbers(self):   # if the iFrame does not have an id or name, use its number to locate it. 
        self.driver.switch_to.frame(0)      # if there is only one iFrame, its number is 0
        return self                         # if there are multiple iFrames, find them by their index number (by order of appearance - ex: higher in the page lower their index number is)
    def switchToIframeUsingID(self):
        self.driver.switch_to.frame(self._iframe_id)
        return self
    def switchToIframeUsingName(self):
        self.driver.switch_to.frame(self._iframe_name)
        return self

    def switchBackToParentFrame(self):
        self.driver.switch_to.default_content()
        return self
    # Methods
    def switchToIframePerformSomeActionSwitchBackToParentFrame(self):
        self.switchToIframeUsingNumbers()
        # The elements of the iframe are now accessible by selenium webdriver 
        # perform the action
        searchBox = self.driver.find_element(By.ID, self._search_box_selector)
        searchBox.send_keys("python")
        # Switch back to the parent frame
        driver.switchBackToParentFrame()
        return self

    # Assertions
    def switchToIframeVerifyThatSearchBoxWorkedSwitchBackToParentFrame(self):
        self.switchToIframeUsingNumbers()
        # elements of the iframe are now available for selenium to perform asssertions on 
        course = self.waitForElement(self._python_course_selector, locatorType="xpath")
        result = course.is_displayed()
        self.verify(result, "Passed", "Search box did not work correctly")
        # Switch back to the parent frame
        self.switchBackToParentFrame()
        return self

