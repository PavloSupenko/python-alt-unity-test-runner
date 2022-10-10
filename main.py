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
tests = [
    "system_dialogs_skip_test.py",
    "privacy_policy_skip_test.py",
    "questionnaire_skip_test.py",
    "purchase_menu_open_test.py"
]

for testName in tests:
    enterArgsString = f"tests/examples/{testName} -k enter -s --junit-xml $DEVICEFARM_LOG_DIR/{testName}.enter.xml"
    enterArgs = enterArgsString.split(" ")
    enterRetCode = pytest.main(enterArgs)
    print(f"Ret code for: {testName}.enter is: {enterRetCode}")

    time.sleep(2)

    exitArgsString = f"tests/examples/{testName} -k exit -s --junit-xml $DEVICEFARM_LOG_DIR/{testName}.exit.xml"
    exitArgs = exitArgsString.split(" ")
    exitRetCode = pytest.main(exitArgs)
    print(f"Ret code for: {testName}.exit is: {exitRetCode}")
