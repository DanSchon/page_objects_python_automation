from selenium.webdriver.common.by import By 
import utilities.custom_logger as cl
import logging
import unittest
from base.basepage import BasePage

class IndexPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators 
    _search_bar = "search-courses"
    _course = "//div[contains(@class,'course-listing-title') and contains(text(),'{0}')]"  #dynamic xpath - the '{0}' will be substituted with an argument containing the actual text
    _all_courses = "course-listing-title"
    _enroll_button = "enroll-button-top"
    _cc_num = "cc_field"
    _cc_exp = "cc-exp"
    _cc_cvv = "cc_cvc"
    _submit_button = "//div[@id='new_card']//button[contains(text(),'Enroll in Course')]"
    _enroll_error_message = "//div[@id='new_card']//div[contains(text(),'The card number is not a valid credit card number.')]"

    # Selectors
    def getSearchBar(self):
        return self.driver.find_element(By.ID, self._search_bar)
    def getCourse(self, fullCourseName):
        return self.driver.find_element(By.XPATH, self._course.format(fullCourseName))   # fullCourseName is the text that replaxes '{0}' in the dynamic xpath
    def getEnrollButton(self):
        return self.driver.find_element(By.ID, self._enroll_button)
    def getCreditCardNumField(self):
        return self.driver.find_element(By.ID, self._cc_num)
    def getCreditCardExpField(self):
        return self.driver.find_element(By.ID, self._cc_exp)
    def getCreditCardCvvField(self):
        return self.driver.find_element(By.ID, self._cc_cvv)
    def getSubmitButton(self):
        return self.driver.find_element(By.XPATH, self._submit_button)
    def waitForEnrollErrorMessage(self):
        messageElement = self.waitForElement(self._enroll_error_message, locatorType="xpath")
        return messageElement
    def getTitle(self):
        return self.driver.title

    # Actions
    def enterCourseNameInSearchBar(self, name):
        self.getSearchBar().send_keys(name)
        return self
    def selectCourseToEnroll(self, fullCourseName):
        self.getCourse(fullCourseName).click()
        return self
    def clickOnEnrollButton(self):
        self.getEnrollButton().click()
    def enterCardNum(self, num):
        self.getCreditCardNumField().send_keys(num)
    def enterCardExp(self, exp):
        self.getCreditCardExpField.send_keys(exp)
    def enterCardCVV(self, cvv):
        self.getCreditCardCvvField.send_keys(cvv)
    def clickEnrollSubmitButton(self):
        self.getSubmitButton().click()

    # Methods
    def enterCreditCardInformation(self, num, exp, cvv):
        self.enterCardNum(num)
        self.enterCardExp(exp)
        self.enterCardCVV(cvv)
        return self

    def enrollInCourse(self, num="", exp="", cvv=""):
        self.clickOnEnrollButton()
        self.webScroll(direction="down")
        self.enterCreditCardInformation(num, exp, cvv)
        self.clickEnrollSubmitButton()
        return self

    # Assertions    
    def verifyEnrollFailed(self):
        errorMessageElement = self.waitForEnrollErrorMessage()
        result = errorMessageElement.is_displayed()
        self.verify(result, "Passed", "Enrollment Failed Verification")
