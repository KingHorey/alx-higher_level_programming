#!/usr/bin/python3

import unittest
from models.base import *
from models.rectangle import *
from models.square import *
""" Import unittest module to test case"""


class TestBase(unittest.TestCase):
    """Unittest cased for base.py"""

    def test_none(self):
        b1 = Base(12)
        b2 = Base()
        b3 = Base()
        self.assertEqual(12, b1.id)
        self.assertNotEqual(Base._Base__nb_objects, b2.id - 1)
        self.assertNotEqual(Base._Base__nb_objects, b3.id - 1)

    def test_str_id(self):
        b1 = Base()
        b1.id = "hello"
        self.assertEqual("hello", b1.id)

    def test_list_id(self):
        b1 = Base()
        b1.id = [1, 2, 4]
        self.assertEqual([1, 2, 4], b1.id)

    def test_tuple(self):
        b1 = Base()
        b1.id = (1, 2)
        self.assertEqual((1, 2), b1.id)

    def test_dict(self):
        b1 = Base()
        b1.id = {'h': 4, 'k': 5}
        self.assertEqual({'h': 4, 'k': 5}, b1.id)

    def test_bool(self):
        b1 = Base()
        b1.id = True
        self.assertEqual(True, b1.id)

    def test_to_jsonstr(self):
        info1 = {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8}
        info2 = {'x': 4, 'width': 11, 'id': 2, 'height': 4, 'y': 2}
        self.assertEqual(str, type(Base.to_json_string([info1])))
        self.assertEqual(str, type(Base.to_json_string([info1])))
        self.assertEqual(str, type(Base.to_json_string([info1, info2])))

    def test_to_json(self):
        info = Rectangle(1, 3, 4, 5)
        info2 = Rectangle(4, 5, 12, 13)
        info = info.to_dictionary()
        info2 = info2.to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([info])))
        self.assertEqual(str, type(Base.to_json_string([info, info2])))
        self.assertEqual("[]", Base.to_json_string(None))


