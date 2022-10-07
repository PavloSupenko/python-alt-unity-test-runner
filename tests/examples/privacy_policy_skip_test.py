import time
from altunityrunner import By
from tests.base.altunity_base_test import AltUnityBaseTest


class TestPrivacyPolicySkip(AltUnityBaseTest):

    def test_enter(self):
        if self.isIosPlatform:
            return

        print("Finding policy accept button")
        acceptButton = self.altUnityDriver.wait_for_object(By.NAME, 'ButtonOk')

        print("Tap on policy accept button")
        acceptButton.tap()

        time.sleep(3)

    def test_exit(self):
        if self.isIosPlatform:
            return

        print("Finding again policy accept button")
        self.altUnityDriver.wait_for_object_to_not_be_present(By.NAME, 'ButtonOk')
