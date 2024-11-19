import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from triangle import area, perimeter


def test_area(self):
    self.assertEqual(area(5, 12, 13), 30)


def test_area_invalid(self):
    with self.assertRaises(TypeError):
        area(5, 12, "13")


def test_invalid_size_area(self):
    with self.assertRaises(TypeError):
        area(5, 12)


def test_perimeter(self):
    self.assertEqual(perimeter(5, 12, 13), 30)


def test_perimeter_invalid(self):
    with self.assertRaises(TypeError):
        perimeter(5, 12, "13")
            

def test_invalid_size_perimeter(self):
    with self.assertRaises(TypeError):
        perimeter(5, 12)
            

if __name__ == '__main__':
    unittest.main()
