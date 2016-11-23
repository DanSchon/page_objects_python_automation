from pages.actions.mouse_hovering_page import MouseHoveringPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class MouseHoveringTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.page = MouseHoveringPage(self.driver)

    @pytest.mark.run(order=1)    
    def test_logoutSuccessfully(self):
        self.page
            .hoverMouseOverDropdownAndClickLogoutElementFromDropdownList()
            .verifyUserLoggedOutSuccessfully()