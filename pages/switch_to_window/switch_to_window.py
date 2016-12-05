from selenium.webdriver.common.by import By 
import utilities.custom_logger as cl
import logging
import unittest
from base.basepage import BasePage


class SwitchToWindow(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver 

    # Locators
    _open_window_button = "openwindow"

    # Selectors
    def getParentWindowHandle(self):
        return self.driver.current_window_handle  

    def getOpenWindowButton(self):
        return self.driver.find_element(By.ID, self._open_window_button)

    # Actions
    def clickOpenWindowButton(self):
        self.getOpenWindowButton.click()
        return self 

    # Methods
    def switchToOtherHandleAndPerformSomeAction(self):
        # identify main-window/parent handle
        parentHandle = self.getParentWindowHandle()
        # Find all handles, there should two handles after clicking open window
        handles = self.driver.window_handles
        # Switch to other window handle and search course
        for handle in handles:
            if handle != parentHandle:       # if this doesn't work try: if handle not in parentHandle:
                self.driver.switch_to.window(handle)
                # perform action
                searchBox = self.driver.find_element(By.ID, self._search_box_selector)
                searchBox.send_keys("python")
                break
        return self

    # Assertions
    def VerifyThatSearchBoxWorkedThenCloseHandleAndSwitchBackToParentHandle(self):
        # elements of the other window are still available for selenium to perform asssertions on 
        course = self.waitForElement(self._python_course_selector, locatorType="xpath")
        result = course.is_displayed()
        self.verify(result, "Passed", "Search box did not work correctly")
        # close other handle
        self.driver.close()
        # switch back to Main-Window/Parent handle
        parentHandle = self.getParentWindowHandle()
        self.driver.switch_to.window(parentHandle)
        return self