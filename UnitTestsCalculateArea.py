import math
import unittest
import CalculateArea


class TestCalculateArea(unittest.TestCase):
    def test_circle_area(self):
        self.assertEqual(CalculateArea.Circle(math.pi).area(), math.pi ** 3)

    def test_invalid_triangle_init(self):
        self.assertRaises(ValueError, CalculateArea.Triangle, 3, 4, 8)

    def test_valid_triangle_area(self):
        self.assertEqual(CalculateArea.Triangle(3, 4, 5).area(), 6)

    def test_is_right_triangle(self):
        self.assertTrue(CalculateArea.Triangle(3, 4, 5).is_right_triangle())
        self.assertFalse(CalculateArea.Triangle(3, 4, 6).is_right_triangle())

    def test_not_implemented_shape_area(self):
        class NotImplementedShape(CalculateArea.Shape):
            pass
        self.assertRaises(NotImplementedError, NotImplementedShape().area)

    def test_without_knowing_type_of_shape_area(self):
        shapes = [CalculateArea.Circle(math.pi ** 2), CalculateArea.Triangle(3, 4, 5)]
        self.assertEqual(shapes[0].area(), math.pi ** 5)
        self.assertEqual(shapes[1].area(), 6)

    def test_is_right_triangle_floating_point(self):
        self.assertTrue(CalculateArea.Triangle(math.sqrt(2), math.sqrt(7), 3).is_right_triangle())
