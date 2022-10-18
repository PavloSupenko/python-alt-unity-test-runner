import os
import platform
from tests_runner.android_tests_runner import AndroidTestsRunner
from tests_runner.arguments import ArgumentsReader
from tests_runner.data_structures.tree.test_tree_builder import TestTreeBuilder
from tests_runner.data_structures.tree.test_tree_executor import TestTreeExecutor

argumentsReader = ArgumentsReader()
androidTestsRunner = AndroidTestsRunner(argumentsReader)

print(f"os.name: {os.name}")
print(f"platform.system: {platform.system()}")
print(f"platform.release: {platform.release()}")

androidTestsRunner.run_appium_session("", "", "")

testTree = TestTreeBuilder('tests.yml').build()
generalArtifactsDirectory = os.environ['DEVICEFARM_LOG_DIR']
testLogsDirectory = os.path.join(generalArtifactsDirectory, "Logs")

testTreeExecutor = TestTreeExecutor(testTree, testLogsDirectory)
testTreeExecutor.execute()
