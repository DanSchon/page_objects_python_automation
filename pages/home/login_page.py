from selenium.webdriver.common.by import By 
import utilities.custom_logger as cl
import logging

class LoginPage(BasePage):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"
    _user_icon = "//*[@id='navbar']//span[text()='User Settings']"
    _login_error_message = "//div[contains(text(),'Invalid email or password')]"

    # Selectors
    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)
    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)
    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._user_password)
    def getLoginButton(self):
        return self.driver.find_element(By.NAME, self._login_button)
    def getUserIcon(self):
        return self.driver.find_element(By.XPATH, self._user_icon)
    def getLoginErrorMessage(self):
        return self.driver.find_element(By.XPATH, self._login_error_message)
    def getTitle(self):
        return self.driver.title

    # Actions
    def clickLoginLink(self):
        self.getLoginLink().click()
        self.log.info("clicked on login link")
    def enterEmail(self, email):
        self.getEmailField.send_keys(email)
        self.log.info("entered email: " + email)
    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)
        self.log.info("entered password: " + password)
    def clickLoginButton(self):
        self.getLoginButton.click()
        self.log.info("clicked on login button")

    # Methods
    def login(self, email="", password=""):     # made the parameters optional so we can reuse the same method with 0, 1, or 2 arguments
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    # Assertions
    def verifyLoginPageTitle(self):
        title = self.getTitle()
        if title == "Sample Page Title":
            result = True
        else:
            result = False
        self.verify(result, "Passed", "Incorrect Page Title")
    def verifyLoginSuccessful(self):
        userIcon = self.getUserIcon()
        result = self.isElementPresent(userIcon)
        self.verify(result, "Passed", "Login Failed")
    def verifyLoginFailed(self):
        errorMessage = self.getLoginErrorMessage()
        result = self.isElementPresent(errorMessage)
        self.verify(result, "Passed", "Logged in Invalidly")