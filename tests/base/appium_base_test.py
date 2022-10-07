import unittest
from tests.drivers.appium_existing_driver import AppiumExistingDriver


class AppiumBaseTest(unittest.TestCase):

    def setUp(self):
        appiumExistingDriver = AppiumExistingDriver()
        self.appiumDriver = appiumExistingDriver.webDriver
        self.isIosPlatform = appiumExistingDriver.isIosPlatform
        self.isAndroidPlatform = appiumExistingDriver.isAndroidPlatform
