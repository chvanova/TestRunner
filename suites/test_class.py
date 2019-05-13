from TestRunner import skip


class TestClass:
    """
    This is test class. All methods that start with test_ should be executed.
    """

    def __init__(self):
        self.some_var = None

    def setup(self):
        self.some_var = 'Some var'

    @skip
    def test_number_1(self):
        pass

    def test_number_2(self):
        assert False

    def test_number_3(self):
        raise FileNotFoundError

    def test_number_4(self):
        pass

    def test_number_5(self):
        self.setup()
        pass
