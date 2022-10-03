import os
import time
from appium import webdriver
from tests_runner.tests_runner import TestsRunnerBase


class AndroidTestsRunner(TestsRunnerBase):

    def isDeviceConnected(self, deviceNumber):
        adbPath = self.argumentsReader.arguments.adb
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

    def setupPortForwarding(self, deviceId, tcpLocalPort, tcpDevicePort):
        pass

    def runAppiumServer(self, hostPlatform):
        pass

    def runAppiumSession(self, deviceId, buildPath, bundle):
        desired_caps = {}
        driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        print("Appium driver started. Waiting a few seconds to go next.")
        time.sleep(5)

    def stopAppiumSession(self):
        pass
