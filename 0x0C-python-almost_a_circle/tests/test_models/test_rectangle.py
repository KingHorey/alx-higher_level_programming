#!/usr/bin/python3

import unittest
from models.base import *
from models.rectangle import *
from models.square import *
""" Import unittest module to test case"""


class TestBase(unittest.TestCase):
    """Unittest cased for base.py"""


    def test_setter(self):
        r1 = Rectangle(3, 1)
        r2 = Rectangle(4, 5)
        self.assertIsInstance(r2.width, int)
        self.assertIsInstance(r1.height, int)
        self.assertIsInstance(r2.height, int)
        self.assertIsInstance(r1.width, int)

    def test_exception(self):
        r1 = Rectangle(5, 5)
        with self.assertRaises(TypeError):
            r1.width = "w"
        with self.assertRaises(TypeError):
            r1.height = "5"
        with self.assertRaises(ValueError):
            r1.width = 0
        with self.assertRaises(ValueError):
            r1.height = 0
        with self.assertRaises(ValueError):
            r1.x = -1
        with self.assertRaises(ValueError):
            r1.y = -7


