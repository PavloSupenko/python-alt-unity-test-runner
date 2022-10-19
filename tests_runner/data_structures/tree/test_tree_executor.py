import os
import time
import pytest
from tests_runner.data_structures.tree.test_tree import TestTree
from tests_runner.test_result_info import TestResultInfo


class TestTreeExecutor:
    def __init__(self, test_tree: TestTree, artifacts_directory: str):
        self._root = test_tree
        self._artifacts_directory = artifacts_directory
        self._enter_test_method_name = 'test_enter'
        self._exit_test_method_name = 'test_exit'
        self._test_results = []

    def execute_tree(self):
        self._current_test_number = 1
        self.__execute_sub_tree(self._root, 1)
        return self._test_results

    def __execute_sub_tree(self, node: TestTree, nesting_level: int):
        is_enter_test_succeed = self.__execute_node(node, self._enter_test_method_name, nesting_level)
        if not is_enter_test_succeed:
            print("Enter test failed so child tests and exit one will not be executed")

        if node.has_children() and is_enter_test_succeed:
            for sub_node in node.children:
                self.__execute_sub_tree(sub_node, nesting_level + 1)

        if is_enter_test_succeed:
            self.__execute_node(node, self._exit_test_method_name, nesting_level)

    def __execute_node(self, node: TestTree, method_name: str, nesting_level):
        # It means that test node is just container for children tests. So 'True' returns like test executed successfully
        if node.test_name is None:
            return True

        test_class_name = node.test_name
        test_directory_name = f"{self._current_test_number}.{str(test_class_name).replace('/', '_')}.{method_name}"
        test_artifacts_path = os.path.join(self._artifacts_directory, 'tests', test_directory_name)
        test_log_path = os.path.join(test_artifacts_path, 'pytest_log.xml')

        print(f"Executing test: {test_class_name}. Artifacts directory: {test_artifacts_path}")

        os.environ["CUSTOM_CURRENT_TEST_DIR"] = test_artifacts_path
        args_string = f"tests/{test_class_name}.py -k {method_name} -s --junit-xml {test_log_path}"
        args = args_string.split(" ")
        return_code = pytest.main(args)

        # Simple waiting between tests. May be redundant and deleted in future
        time.sleep(2)

        test_success = return_code == 0
        print(f"Saving test result data (test name: {test_directory_name}, success: {test_success}), artifacts: {test_artifacts_path}, nesting: {nesting_level}")
        self._test_results.append(TestResultInfo(test_directory_name, test_success, test_artifacts_path, nesting_level))

        print(f"Return code for {node.test_name}::{method_name} is {return_code}")
        self._current_test_number += 1
        return test_success
