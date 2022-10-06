import time
from appium.webdriver.common.appiumby import AppiumBy
from tests.base.appium_base_test import AppiumBaseTest


class TestSystemDialogsSkip(AppiumBaseTest):

    def test_enter(self):
        if self.isAndroidPlatform:
            return

        time.sleep(5)
        firebaseWarningSkipButton = self.appiumDriver.find_element(by=AppiumBy.ACCESSIBILITY_ID, value='OK')
        firebaseWarningSkipButton.click()

    def test_exit(self):
        assert True
