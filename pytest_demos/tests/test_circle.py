from src import shapes
import math
class TestCircle():
    
    def setup_method(self, method):
        print(f"\nSetting up for {method.__name__}")
        self.circle = shapes.Circle(10)

    def teardown_method(self, method):
        print(f"Tearing down for {method.__name__}")
        # cleanup actions e.g. delete object (anyway donw automatically)
        del self.circle

    def test_area(self):
        assert self.circle.area() == math.pi * self.circle.radius ** 2

    def test_perimeter(self):
        assert self.circle.perimeter() == 2 * math.pi * self.circle.radius
    
    def test_circle_area_not_same_as_rectangle_area(self, my_rectangle):
        assert self.circle.area() != my_rectangle.area()