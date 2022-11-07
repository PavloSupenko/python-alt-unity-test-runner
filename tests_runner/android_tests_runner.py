import os
import time
from appium import webdriver
from tests_runner.base.tests_runner import TestsRunnerBase


class AndroidTestsRunner(TestsRunnerBase):

    def is_device_connected(self, deviceNumber):
        adbPath = self.reader.arguments.adb
        arguments = "devices"
        print(f"Executing command: {adbPath} {arguments}")

        commandOutput = os.popen(f'"{adbPath}" {arguments}').read()

        devices = []
        outputLines = commandOutput.splitlines()
        for line in outputLines:
            if line and "device" in line and "List" not in line:
                devices.append(line.split('\t')[0])

        if len(devices) == 0:
            print("No devices connected to execute tests.")
            return ""

        print("Device ID's found:")
        for device in devices:
            print(device)

        if len(devices) < deviceNumber:
            print(f"Not enough devices to execute with target device number: {deviceNumber}.")
            return ""

        deviceId = devices[deviceNumber - 1]
        return deviceId

    def setup_port_forwarding(self, deviceId, tcpLocalPort, tcpDevicePort):
        pass

    def run_appium_server(self, hostPlatform):
        pass

    def run_appium_session(self, deviceId, buildPath, bundle):
        appium_port_number = int(os.environ["APPIUM_PORT"])
        driver = webdriver.Remote(f"http://localhost:{appium_port_number}/wd/hub", desired_capabilities={})
        print("Appium driver started. Waiting a few seconds to go next.")
        time.sleep(5)

    def stop_appium_session(self):
        pass
