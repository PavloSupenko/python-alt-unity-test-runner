from TestsRunner.androidTestsRunner import AndroidTestsRunner
from TestsRunner.arguments import ArgumentsReader

argumentsReader = ArgumentsReader()

androidTestsRunner = AndroidTestsRunner(argumentsReader)
androidTestsRunner.isDeviceConnected(3)
