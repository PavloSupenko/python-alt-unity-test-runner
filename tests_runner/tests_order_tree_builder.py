from typing import List
import yaml


class TestsOrderTreeBuilder:

    def __init__(self, filename: str):
        self.filename = filename

    def get_tests_order(self) -> List[str]:
        with open(self.filename) as testsOrderFile:
            testsOrder = yaml.safe_load(testsOrderFile)

        testsList = []

        for test in testsOrder:
            self.add_subtests_to_order_list(test, testsList)

        return testsList

    def add_subtests_to_order_list(self, testData, testsList: list):
        testsList.append(f"{testData['test']}::test_enter")

        if 'subtests' in testData:
            subtests = testData['subtests']
            for subtest in subtests:
                self.add_subtests_to_order_list(subtest, testsList)

        testsList.append(f"{testData['test']}::test_exit")

