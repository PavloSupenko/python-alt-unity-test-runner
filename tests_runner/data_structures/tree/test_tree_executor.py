import os
import time
import pytest
from tests_runner.data_structures.tree.test_tree import TestTree


class TestTreeExecutor:
    def __init__(self, test_tree: TestTree, logs_directory: str):
        self._root = test_tree
        self._logs_directory = logs_directory
        self._enter_test_method_name = 'test_enter'
        self._exit_test_method_name = 'test_exit'

    def execute(self):
        self.__execute_test_node(self._root)

    def __execute_test_node(self, node: TestTree):
        is_enter_test_succeed = self.__execute_test(node, self._enter_test_method_name)
        if not is_enter_test_succeed:
            print("Enter test failed so child tests and exit one will not be executed")

        if node.has_children() and is_enter_test_succeed:
            for sub_node in node.children:
                self.__execute_test_node(sub_node)

        if is_enter_test_succeed:
            self.__execute_test(node, self._exit_test_method_name)

    def __execute_test(self, node: TestTree, method_name: str):
        # It means that test node is just container for children tests. So 'True' returns like test executed successfully
        if node.test_name is None:
            return True

        return_code = self.__execute_pytest(node.test_name, method_name)
        print(f"Return code for {node.test_name}::{method_name} is {return_code}")
        return return_code == 0

    def __execute_pytest(self, test_class_name, test_method_name):
        currentTestLogPath = os.path.join(self._logs_directory, test_class_name, test_method_name + '.xml')

        args_string = f"tests/{test_class_name}.py -k {test_method_name} -s --junit-xml {currentTestLogPath}"
        args = args_string.split(" ")
        return_code = pytest.main(args)

        # Simple waiting between tests. May be redundant and deleted in future
        time.sleep(2)

        return return_code
