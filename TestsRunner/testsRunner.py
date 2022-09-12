from abc import ABCMeta, abstractmethod


class TestsRunnerBase(metaclass=ABCMeta):

    def __init__(self, argumentsReader):
        self._argumentsReader = argumentsReader

    @property
    def argumentsReader(self):
        return self._argumentsReader

    @abstractmethod
    def isDeviceConnected(self, deviceNumber):
        pass

    @abstractmethod
    def setupPortForwarding(self, deviceId, tcpLocalPort, tcpDevicePort):
        pass

    @abstractmethod
    def runAppiumServer(self, hostPlatform):
        pass

    @abstractmethod
    def runAppiumSession(self, deviceId, buildPath, bundle):
        pass

    @abstractmethod
    def stopAppiumSession(self):
        pass
