class TestResultInfo:
    def __init__(self, name, success, artifacts_path, nesting_level):
        self.name = name
        self.success = success
        self.artifacts_path = artifacts_path
        self.nesting_level = nesting_level
