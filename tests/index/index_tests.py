from pages.index.index_page import IndexPage
from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class IndexTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.index_page = IndexPage(self.driver)
        self.login_page = LoginPage(self.driver)

    @pytest.mark.run(order=1)    
    def test_validLogin(self):
        self.login_page
            .login("test@email.com", "abcabc")
            .verifyLoginSuccessful()
            
    @pytest.mark.run(order=2)
    def test_invalidEnrollment(self):
        self.index_page
            .enterCourseNameInSearchBar("JavaScript")
            .selectCourseToEnroll("JavaScript for beginners")
            .enrollInCourse(num="10", exp="1220", cvv="10")
            .verifyEnrollFailed()