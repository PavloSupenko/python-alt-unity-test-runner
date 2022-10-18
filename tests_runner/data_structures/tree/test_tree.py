class TestTree:
    def __init__(self, test_name):
        self.test_name = test_name
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)

    def has_children(self):
        return len(self.children) > 0
