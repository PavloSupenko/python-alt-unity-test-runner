import yaml
from tests_runner.data_structures.tree.test_tree import TestTree


class TestTreeBuilder:
    def __init__(self, filename: str):
        self.filename = filename

    def build(self) -> TestTree:
        with open(self.filename) as testsOrderFile:
            tests_order_info = yaml.safe_load(testsOrderFile)

        # Creating empty root item. It's just container for another test trees
        root_node = TestTree(None)

        for test_info in tests_order_info:
            self.__add_subtests_to_node(root_node, test_info)

        return root_node

    def __add_subtests_to_node(self, parent_node: TestTree, test_info):
        test_name = test_info['test']

        node = TestTree(test_name)
        parent_node.add_child(node)

        if 'subtests' in test_info:
            subtests_info = test_info['subtests']
            for subtest_info in subtests_info:
                self.__add_subtests_to_node(node, subtest_info)
