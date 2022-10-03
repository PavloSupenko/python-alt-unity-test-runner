import time
import unittest
from altunityrunner import By, AltUnityDriver
from tests.drivers.appium_existing_driver import AppiumExistingDriver


class TestAppDialogsSkip(unittest.TestCase):

    def setUp(self):
        appiumExistingDriver = AppiumExistingDriver()
        self.appiumDriver = appiumExistingDriver.webDriver
        self.isIosPlatform = appiumExistingDriver.isIosPlatform
        self.isAndroidPlatform = appiumExistingDriver.isAndroidPlatform

        self.altUnityDriver = AltUnityDriver()

    def tearDown(self):
        self.altUnityDriver.stop()

    def test_skip_app_dialogs(self):
        print("Starting skipping app dialogs test")

        print("Finding policy accept button")
        acceptButton = self.altUnityDriver.wait_for_object(By.NAME, 'ButtonOk')

        print("Tap on policy accept button")
        acceptButton.tap()

        time.sleep(2)

        print("Finding again policy accept button")
        self.altUnityDriver.wait_for_object_to_not_be_present(By.NAME, 'ButtonOk')
