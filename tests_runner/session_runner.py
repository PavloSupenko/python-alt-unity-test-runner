import os
import time
from appium import webdriver


class SessionRunner:
    def __init__(self, appium_port_number):
        self.port = appium_port_number

    def run_appium_session(self):
        driver = webdriver.Remote(f"http://localhost:{self.port}/wd/hub", desired_capabilities={})
        print(f"Appium session started on port: {self.port}. Waiting a few seconds to go next.")
        time.sleep(5)
