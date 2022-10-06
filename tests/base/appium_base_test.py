import unittest
from abc import abstractmethod, ABC
from tests.drivers.appium_existing_driver import AppiumExistingDriver


class AppiumBaseTest(unittest.TestCase, ABC):

    def setUp(self):
        appiumExistingDriver = AppiumExistingDriver()
        self.appiumDriver = appiumExistingDriver.webDriver
        self.isIosPlatform = appiumExistingDriver.isIosPlatform
        self.isAndroidPlatform = appiumExistingDriver.isAndroidPlatform

    @abstractmethod
    def test_enter(self):
        ...

    @abstractmethod
    def test_exit(self):
        ...