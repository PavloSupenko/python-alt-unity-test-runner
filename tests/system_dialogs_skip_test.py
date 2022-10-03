import time
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from tests.drivers.appium_existing_driver import AppiumExistingDriver


class TestSystemDialogsSkip(unittest.TestCase):

    def setUp(self):
        appiumExistingDriver = AppiumExistingDriver()
        self.appiumDriver = appiumExistingDriver.webDriver
        self.isIosPlatform = appiumExistingDriver.isIosPlatform
        self.isAndroidPlatform = appiumExistingDriver.isAndroidPlatform

    def tearDown(self):
        pass

    def test_skip_system_dialogs(self):
        print("Starting skipping system dialogs test")
        time.sleep(5)

        firebaseWarningSkipButton = self.appiumDriver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='OK')
        firebaseWarningSkipButton.click()

        time.sleep(10)

        # if self.isIosPlatform:
        #    print("Platform is iOS - we need to skip Firebase button")

        #    try:
        #        firebaseWarningSkipButton = self.driver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='OK')
        #        firebaseWarningSkipButton.click()

        #        time.sleep(10)
        #    except:
        #        print("No iOS Firebase develop warning message found.")
