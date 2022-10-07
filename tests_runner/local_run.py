import os
import time
import platform
from subprocess import Popen
from tests_runner.arguments import ArgumentsReader
from tests_runner.android_tests_runner import AndroidTestsRunner


argumentsReader = ArgumentsReader()
androidTestsRunner = AndroidTestsRunner(argumentsReader)

deviceId = androidTestsRunner.is_device_connected(1)
if not deviceId:
    exit()

print(f"os.name: {os.name}")
print(f"platform.system: {platform.system()}")
print(f"platform.release: {platform.release()}")

androidTestsRunner.run_appium_session("", "", "")

tests = [
    "system_dialogs_skip_test.py",
    "privacy_policy_skip_test.py",
    "questionnaire_skip_test.py"
]

for testName in tests:
    Popen("py.test tests/examples/" + testName + " -k enter -s --junit-xml $DEVICEFARM_LOG_DIR/system.enter_test.xml",
          shell=True).wait()

    time.sleep(2)

    Popen("py.test tests/examples/" + testName + " -k exit -s --junit-xml $DEVICEFARM_LOG_DIR/system.enter_test.xml",
          shell=True).wait()
