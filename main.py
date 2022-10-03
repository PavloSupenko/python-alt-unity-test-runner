import os
import time

from tests_runner.android_tests_runner import AndroidTestsRunner
from tests_runner.arguments import ArgumentsReader

argumentsReader = ArgumentsReader()

androidTestsRunner = AndroidTestsRunner(argumentsReader)
# deviceId = androidTestsRunner.isDeviceConnected(1)

# if not deviceId:
#     exit()

androidTestsRunner.runAppiumSession("", "", "")
print("Try run tests from code")

commandOutput1 = os.popen('py.test tests/system_dialogs_skip_test.py -s --junit-xml $DEVICEFARM_LOG_DIR/junitreport-1.xml').read()
print(commandOutput1)

time.sleep(3)

commandOutput2 = os.popen('py.test tests/questionnaire_skip_test.py -s --junit-xml $DEVICEFARM_LOG_DIR/junitreport-2.xml').read()
print(commandOutput2)
