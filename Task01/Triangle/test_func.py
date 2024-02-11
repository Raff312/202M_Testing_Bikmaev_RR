import unittest

from triangle_func import IncorrectTriangleSides, get_triangle_type

class TestGetTriangleType(unittest.TestCase):
    def test_equilateral_triangle(self):
        self.assertEqual(get_triangle_type(5, 5, 5), 'equilateral')

    def test_isosceles_triangle(self):
        self.assertEqual(get_triangle_type(4, 4, 6), 'isosceles')

    def test_nonequilateral_triangle(self):
        self.assertEqual(get_triangle_type(3, 4, 5), 'nonequilateral')

    def test_negative_side_length(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(-2, 3, 4)

    def test_impossible_triangle(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(1, 1, 10)

    def test_zero_side_length(self):
        with self.assertRaises(IncorrectTriangleSides):
            get_triangle_type(0, 4, 5)

if __name__ == '__main__':
    unittest.main()