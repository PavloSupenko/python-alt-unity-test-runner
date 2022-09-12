from TestsRunner.testsRunner import TestsRunnerBase


class AndroidTestsRunner(TestsRunnerBase):

    def isDeviceConnected(self, deviceNumber):
        print(f"{self.argumentsReader.arguments.adb}")

    def setupPortForwarding(self, deviceId, tcpLocalPort, tcpDevicePort):
        pass

    def runAppiumServer(self, hostPlatform):
        pass

    def runAppiumSession(self, deviceId, buildPath, bundle):
        pass

    def stopAppiumSession(self):
        pass
