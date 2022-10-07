import time
from altunityrunner import By
from tests.base.altunity_base_test import AltUnityBaseTest


class TestQuestionnaireSkip(AltUnityBaseTest):

    def test_enter(self):
        print("Finding skip survey button")
        skipButton = self.altUnityDriver.wait_for_object(By.NAME, 'Skip')

        print("Tap skip survey button")
        skipButton.tap()

        time.sleep(2)

    def test_exit(self):
        print("Finding skip survey button again")
        self.altUnityDriver.wait_for_object_to_not_be_present(By.NAME, 'Skip')
