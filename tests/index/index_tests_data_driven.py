from pages.index.index_page import IndexPage
from pages.home.login_page import LoginPage
import unittest
import pytest
from ddt import ddt, data, unpack

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterMultipleCoursesTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.courses = RegisterCoursesPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)    
    def test_validLogin(self):
        self.login_page
            .login("test@email.com", "abcabc")
            .verifyLoginSuccessful()

    @pytest.mark.run(order=2)
    @data(("Programming for Dummies", "4242424242424242", "1220", "100"), ("Programming for Geniuses", "2424242424242424", "0120", "200"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.index_page
            .enterCourseNameInSearchBar(courseName)
            .selectCourseToEnroll(courseName)
            .enrollInCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
            .verifyEnrollFailed()
            
        self.index_page.clickOnAllCoursesLink()    # so that next iteration can find search bar successfully


