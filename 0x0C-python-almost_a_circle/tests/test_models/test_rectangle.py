#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import *
from models.square import *
""" Import unittest module to test case"""


class TestBase(unittest.TestCase):
    """Unittest cased for base.py"""

    def test_rect_strings(self):

        """ test square instance and atrributes
        Detailed -
        method tests attributes of a square instance
        and rasies the following error:

        TypeError -
        if x, y, size is not an integer

        ValueError -
        when width, height, is Zero
        when x or y is 0 or negative

        """
        with self.assertRaises(ValueError):
            r = Rectangle(0, 4, 3, 6)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 0, 5, 7)

        with self.assertRaises(ValueError):
            r = Rectangle(5, 3, -1, 5)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 4, 0, -4)

        with self.assertRaises(TypeError):
            r = Rectangle("1", 4)

        with self.assertRaises(TypeError):
            r = Rectangle(1, "4")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 4, "4")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 4, 4, "6")

    def test_setter(self):
        """ tests type of width and height """
        r1 = Rectangle(3, 1)
        r2 = Rectangle(4, 5)
        self.assertIsInstance(r2.width, int)
        self.assertIsInstance(r1.height, int)
        self.assertIsInstance(r2.height, int)
        self.assertIsInstance(r1.width, int)

    def testarea(self):
        r1 = Rectangle(4, 5)
        self.assertEqual(20, r1.area())
