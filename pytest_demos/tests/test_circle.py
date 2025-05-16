
class TestCircle():
    
    def setup_method(self, method):
        print(f"Setting up for {method.__name__}")


    def test_one(self):
        assert True

    def teardown_method(self, method):
        print(f"Tearing down for {method.__name__}")