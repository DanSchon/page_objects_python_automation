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
    _draggable_element = "draggable"
    _droppable_element = "//div[@class='mouse-hover-content']//a[text()='Log Out']"
    _success_message = "//div[contains(@class,'flash-message') and contains(text(),'Element dragged and dropped successfully')]"


    # Selectors
    def draggableElement(self):
        return self.driver.find_element(By.ID, self._draggable_element)
    def droppableElement(self):
        return self.driver.find_element(By.ID, self._droppable_element)
    

    # Actions - Both Work
    def dragAndDropElementToTarget_1(self):
        actions = ActionChains(self.driver)
        actions.drag_and_drop(self.draggableElement(), self.droppableElement()).perform()
        self.log.info("Item was dragged and dropped into target using drag_and_drop action method")
        return self
    def dragAndDropElementToTarget_2(self):
        actions = ActionChains(self.driver)
        actions.click_and_hold(self.draggableElement()).move_to_element(self.droppableElement()).release().perform()
        self.log.info("Item was dragged and dropped into target using action chains")
        return self

    # Methods
    def dragAndDropDraggableElementToDroppableElement(self):
        self.dragAndDropElementToTarget_1()
        # or self.dragAndDropElementToTarget_2() -- both work
        time.sleep(2)
        return self

    # Assertions    
    def verifyUserDraggedAndDroppedElementSuccessfully(self):
        successMessageElement = self.waitForElement(self._success_message, locatorType="xpath")
        result = successMessageElement.is_displayed()
        self.verify(result, "Passed", "Drag and Drop Was Not Successful")