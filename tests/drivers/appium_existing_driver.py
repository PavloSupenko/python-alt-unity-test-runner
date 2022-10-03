import json
import os
import sys
import requests
from appium import webdriver
from appium.webdriver.webdriver import WebDriver
sys.path.append(os.path.dirname(__file__))


class AppiumExistingDriver:
    webDriver = None
    platform = None
    isIosPlatform = False
    isAndroidPlatform = False

    def __init__(self):
        content = requests.get('http://127.0.0.1:4723/wd/hub/sessions').text

        if content is None or content is "":
            print("No Appium sessions found.")
            return

        print(f"Sessions request content: {content}")

        sessionsData = json.loads(content)
        firstSessionId = sessionsData["value"][0]["id"]
        appiumUrl = "http://localhost:4723/wd/hub"

        self.webDriver = self.attach_to_session(appiumUrl, firstSessionId)

        # self.set_up_platform_fields()
        self.isIosPlatform = True
        self.isAndroidPlatform = False

    def set_up_platform_fields(self):
        # platform is [Android / iOS]
        self.platform = self.webDriver.capabilities['platformName']
        print(f"Appium platform: {self.platform}")

        self.isAndroidPlatform = self.platform == 'Android'
        self.isIosPlatform = self.platform == 'iOS'

    def attach_to_session(self, executor_url, session_id):
        original_execute = WebDriver.execute

        def new_command_execute(self, command, params=None):
            if command == 'newSession':
                return {'value': None, 'sessionId': session_id}
            else:
                return original_execute(self, command, params)

        WebDriver.execute = new_command_execute
        driver = webdriver.Remote(command_executor=executor_url, desired_capabilities={}, direct_connection=False)
        driver.session_id = session_id
        WebDriver.execute = original_execute
        return driver
