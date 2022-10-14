import os
import time
import platform
import pytest
from tests_runner.arguments import ArgumentsReader
from tests_runner.android_tests_runner import AndroidTestsRunner

argumentsReader = ArgumentsReader()
androidTestsRunner = AndroidTestsRunner(argumentsReader)

print(f"os.name: {os.name}")
print(f"platform.system: {platform.system()}")
print(f"platform.release: {platform.release()}")

androidTestsRunner.run_appium_session("", "", "")
testsOrderFile = open("tests.txt", "r")
testNames = testsOrderFile.read().split('\n')

print('Test names found:')
testNumber = 1
for testName in testNames:
    print(f"{testNumber}.{testName}")
    testNumber += 1


generalArtifactsDirectory = os.environ['DEVICEFARM_LOG_DIR']
testLogsDirectory = os.path.join(generalArtifactsDirectory, "Logs")

for testName in testNames:
    currentTestLogDirectory = os.path.join(testLogsDirectory, testName)
    currentEnterTestLogPath = os.path.join(currentTestLogDirectory, "enter.xml")
    currentExitTestLogPath = os.path.join(currentTestLogDirectory, "exit.xml")

    enterArgsString = f"tests/{testName}.py -k enter -s --junit-xml {currentEnterTestLogPath}"
    enterArgs = enterArgsString.split(" ")
    enterRetCode = pytest.main(enterArgs)
    print(f"Return code for: {testName}.enter is: {enterRetCode}")

    time.sleep(2)

    exitArgsString = f"tests/{testName}.py -k exit -s --junit-xml {currentExitTestLogPath}"
    exitArgs = exitArgsString.split(" ")
    exitRetCode = pytest.main(exitArgs)
    print(f"Return code for: {testName}.exit is: {exitRetCode}")
