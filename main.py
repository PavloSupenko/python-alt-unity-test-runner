import os
from tests_runner.report_builder import ReportBuilder

artifacts_directory = os.environ['DEVICEFARM_LOG_DIR']
report_builder = ReportBuilder(test_render_results, artifacts_directory).create_report()
