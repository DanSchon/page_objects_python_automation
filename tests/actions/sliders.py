from pages.actions.slider_page import SliderPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class SliderTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.page = SliderPage(self.driver)

    @pytest.mark.run(order=1)    
    def test_MoveSliderHandleSuccessfully(self):
        self.page
            .moveSliderHandleToTheMiddleOfTheSlideBar()
            .verifyUserMovedSliderHandleSuccessfully()           

