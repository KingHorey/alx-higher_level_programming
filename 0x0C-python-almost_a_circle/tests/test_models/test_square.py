#!/usr/bin/python3

""" import unittest, Base, Square and Rectangle modules """
import unittest
from models.base import *
from models.rectangle import *
from models.square import *

class TestCases(unittest.TestCase):

    def test_sq_args(self):
        """ test square instance and atrributes
        Detailed -
        method tests attributes of a square instance
        and rasies the following error:

        TypeError -
        if x, y, size is not an integer

        ValueError -
        when size, is Zero
        when x or y is 0 or negative

        """
        with self.assertRaises(TypeError):
            s = Square("1", 4)

        with self.assertRaises(TypeError):
            r = Square(1, "4")

        with self.assertRaises(TypeError):
            r = Square(1, "3", 5)

        with self.assertRaises(TypeError):
            r = Square(1, 4, "6")

        with self.assertRaises(ValueError):
            r = Square(0, 4, 3)

        with self.assertRaises(ValueError):
            r = Square(1, -1, 5)

