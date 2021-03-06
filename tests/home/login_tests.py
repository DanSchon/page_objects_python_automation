from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)


    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp
            .login("test@email.com", "abcabc")
            .verifyLoginSuccessful()

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp
            .login(password="abcabc")
            .verifyLoginFailed()