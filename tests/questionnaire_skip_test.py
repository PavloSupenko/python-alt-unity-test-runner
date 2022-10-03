import time
import unittest
from altunityrunner import By, AltUnityDriver


class QuestionnaireSkipTest(unittest.TestCase):

    def setUp(self):
        self.altUnityDriver = AltUnityDriver(host="127.0.0.1", port=13000, enable_logging=True, timeout=30)

    def test_skip_questionnaire(self):
        print("Starting skipping questionnaire")

        time.sleep(10)

        print("Finding skip button")
        acceptButton = self.altUnityDriver.wait_for_object(By.NAME, 'Skip')

        print("Tap skip button")
        acceptButton.tap()

        time.sleep(2)

        print("Finding skip button again")
        self.altUnityDriver.wait_for_object_to_not_be_present(By.NAME, 'Skip')
