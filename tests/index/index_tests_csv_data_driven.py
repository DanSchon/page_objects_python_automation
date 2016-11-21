from pages.index.index_page import IndexPage
from pages.home.login_page import LoginPage
import unittest
import pytest
from ddt import ddt, data, unpack
from utilities.read_csv_data import getCSVData

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
@ddt
class RegisterCoursesCSVDataTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.index_page = IndexPage(self.driver)
        self.login_page = LoginPage(self.driver)

    @pytest.mark.run(order=1)    
    def test_validLogin(self):
        self.login_page
            .login("test@email.com", "abcabc")
            .verifyLoginSuccessful()

    def setUp(self):
        self.driver.find_element_by_link_text("All Courses").click()

    @pytest.mark.run(order=1)
    @data(*getCSVData("/Users/danielschonfeld/Desktop/page_objects_python/testdata.csv"))
    @unpack
    def test_invalidEnrollment(self, courseName, ccNum, ccExp, ccCVV):
        self.index_page
            .enterCourseNameInSearchBar(courseName)
            .selectCourseToEnroll(courseName)
            .enrollInCourse(num=ccNum, exp=ccExp, cvv=ccCVV)
            .verifyEnrollFailed()
            
        self.index_page.clickOnAllCoursesLink()    # so that next iteration can find search bar successfully