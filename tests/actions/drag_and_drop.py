from pages.actions.drag_and_drop_page import DragAndDropPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class DragAndDropTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def objectSetup(self, oneTimeSetUp):
        self.page = DragAndDropPage(self.driver)

    @pytest.mark.run(order=1)    
    def test_dragAndDropSuccessfully(self):
        self.page
            .dragAndDropDraggableElementToDroppableElement()
            .verifyUserDraggedAndDroppedElementSuccessfully()