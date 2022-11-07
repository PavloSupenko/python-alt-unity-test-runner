import os
import platform
from tests_runner.report_builder import ReportBuilder
from tests_runner.session_runner import SessionRunner
from tests_runner.data_structures.tree.test_tree_builder import TestTreeBuilder
from tests_runner.data_structures.tree.test_tree_executor import TestTreeExecutor


print(f"os.name: {os.name}")
print(f"platform.system: {platform.system()}")
print(f"platform.release: {platform.release()}")

appium_port_number = int(os.environ["APPIUM_PORT"])
artifacts_directory = os.environ['DEVICEFARM_LOG_DIR']

session_runner = SessionRunner(appium_port_number)
session_runner.run_appium_session()

test_tree = TestTreeBuilder('tests.yml').build()
test_tree_executor = TestTreeExecutor(test_tree, artifacts_directory)
test_render_results = test_tree_executor.execute_tree()

report_builder = ReportBuilder(test_render_results, artifacts_directory).create_report()
