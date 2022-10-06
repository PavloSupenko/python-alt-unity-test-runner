import os
import platform
import time
from subprocess import Popen
from tests_runner.android_tests_runner import AndroidTestsRunner
from tests_runner.arguments import ArgumentsReader

argumentsReader = ArgumentsReader()
androidTestsRunner = AndroidTestsRunner(argumentsReader)

# deviceId = androidTestsRunner.isDeviceConnected(1)
# if not deviceId:
#     exit()

print(f"os.name: {os.name}")
print(f"platform.system: {platform.system()}")
print(f"platform.release: {platform.release()}")

androidTestsRunner.run_appium_session("", "", "")

tests = [
    "system_dialogs_skip_test.py::TestSystemDialogsSkip",
    "privacy_policy_skip_test.py::TestPrivacyPolicySkip",
    "questionnaire_skip_test.py::TestQuestionnaireSkip"
]

for testName in tests:
    Popen("py.test tests/examples/" + testName + "::test_enter -s --junit-xml $DEVICEFARM_LOG_DIR/system.enter_test.xml",
          shell=True).wait()

    time.sleep(2)

    Popen("py.test tests/examples/" + testName + "::test_exit -s --junit-xml $DEVICEFARM_LOG_DIR/system.enter_test.xml",
          shell=True).wait()
