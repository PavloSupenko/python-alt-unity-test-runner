import unittest
from altunityrunner import AltUnityDriver
from tests.drivers.appium_existing_driver import AppiumExistingDriver


class AltUnityBaseTest(unittest.TestCase):

    def setUp(self):
        appiumExistingDriver = AppiumExistingDriver()
        self.appiumDriver = appiumExistingDriver.webDriver
        self.isIosPlatform = appiumExistingDriver.isIosPlatform
        self.isAndroidPlatform = appiumExistingDriver.isAndroidPlatform

        self.altUnityDriver = AltUnityDriver(host="127.0.0.1", port=13000, enable_logging=True, timeout=30)

    def tearDown(self):
        self.altUnityDriver.stop()
