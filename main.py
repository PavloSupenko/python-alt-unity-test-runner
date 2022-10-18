import os
import time
import platform
from pprint import pprint
import pytest
from tests_runner.arguments import ArgumentsReader
from tests_runner.android_tests_runner import AndroidTestsRunner
from tests_runner.tests_order_tree_builder import TestsOrderTreeBuilder

argumentsReader = ArgumentsReader()
androidTestsRunner = AndroidTestsRunner(argumentsReader)

print(f"os.name: {os.name}")
print(f"platform.system: {platform.system()}")
print(f"platform.release: {platform.release()}")

androidTestsRunner.run_appium_session("", "", "")

tests = TestsOrderTreeBuilder('tests.yml').get_tests_order()
pprint(tests)

generalArtifactsDirectory = os.environ['DEVICEFARM_LOG_DIR']
testLogsDirectory = os.path.join(generalArtifactsDirectory, "Logs")

for test in tests:
    testName = test.split('::')[0]
    testMethod = test.split('::')[1]

    currentTestLogPath = os.path.join(testLogsDirectory, testName, testMethod + '.xml')

    enterArgsString = f"tests/{testName}.py -k {testMethod} -s --junit-xml {currentTestLogPath}"
    enterArgs = enterArgsString.split(" ")
    enterRetCode = pytest.main(enterArgs)
    print(f"Return code for: {testName}.{testMethod} is: {enterRetCode}")

    time.sleep(2)
