from selenium.webdriver.common.by import By 

class LoginPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

    # Selectors
    def getLoginLink(self):
        return self.driver.find_element(By.LINK_TEXT, self._login_link)
    def getEmailField(self):
        return self.driver.find_element(By.ID, self._email_field)
    def getPasswordField(self):
        return self.driver.find_element(By.ID, self._user_password)
    def getLoginButton(self):
        return self.driver.find_element(By.NAME, self._login_button)

    # Actions
    def clickLoginLink(self):
        self.getLoginLink().click()
        print "clicked on login link"
    def enterEmail(self, email):
        self.getEmailField.send_keys(email)
        print "entered email: " + email
    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)
        print "entered password: " + password
    def clickLoginButton(self):
        self.getLoginButton.click()
        print "clicked on login button"

    # Methods
    def login(self, email, password):
        self.clickLoginLink()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()