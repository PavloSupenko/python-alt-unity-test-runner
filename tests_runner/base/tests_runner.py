from abc import abstractmethod, ABC


class TestsRunnerBase(ABC):

    def __init__(self, argumentsReader):
        self._argumentsReader = argumentsReader

    @property
    def reader(self):
        return self._argumentsReader

    @abstractmethod
    def is_device_connected(self, deviceNumber):
        pass

    @abstractmethod
    def setup_port_forwarding(self, deviceId, tcpLocalPort, tcpDevicePort):
        pass

    @abstractmethod
    def run_appium_server(self, hostPlatform):
        pass

    @abstractmethod
    def run_appium_session(self, deviceId, buildPath, bundle):
        pass

    @abstractmethod
    def stop_appium_session(self):
        pass
