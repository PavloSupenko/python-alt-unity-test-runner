import time
from altunityrunner import By
from tests.base.altunity_base_test import AltUnityBaseTest


class TestQuestionnaireSkip(AltUnityBaseTest):

    def test_enter(self):
        print("Finding skip button")
        acceptButton = self.altUnityDriver.wait_for_object(By.NAME, 'Skip')

        print("Tap skip button")
        acceptButton.tap()

        time.sleep(2)

    def test_exit(self):
        print("Finding skip button again")
        self.altUnityDriver.wait_for_object_to_not_be_present(By.NAME, 'Skip')
