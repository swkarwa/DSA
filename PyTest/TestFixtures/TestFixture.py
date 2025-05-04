from traceback import print_tb

class TestFixture:
    def test_module_fixture(self , test_function_fixture):
        assert True

    def test_sample_fixture(self, test_function_fixture):
        assert True

    def test_one(self , test_function_fixture):
        print("Test code")

    def test_two(self, test_function_fixture):
        print("Test code")