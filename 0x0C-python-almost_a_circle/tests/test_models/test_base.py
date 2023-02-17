#!/usr/bin/python3

import unittest
from models.base import *
from models.rectangle import *
from models.square import *


class TestID(unittest.TestCase):
    """ Test ID for base class"""

    def test_none(self):
        b1 = Base(12)
        b2 = Base()
        b3 = Base()
        self.assertEqual(12, b1.id)
        self.assertNotEqual(Base._Base__nb_objects, b2.id - 1)
        self.assertNotEqual(Base._Base__nb_objects, b3.id - 1)

    def test_str_id(self):
        """ test id as a string"""
        b1 = Base()
        b1.id = "hello"
        self.assertEqual("hello", b1.id)

    def test_list_id(self):
        """Test id as a list"""
        b1 = Base()
        b1.id = [1, 2, 4]
        self.assertEqual([1, 2, 4], b1.id)

    def test_tuple(self):
        """Test id as a tuple"""
        b1 = Base()
        b1.id = (1, 2)
        self.assertEqual((1, 2), b1.id)

    def test_dict(self):
        """test id as a dict"""
        b1 = Base()
        b1.id = {'h': 4, 'k': 5}
        self.assertEqual({'h': 4, 'k': 5}, b1.id)

    def test_bool(self):
        """Test id as a bool"""
        b1 = Base()
        b1.id = True
        self.assertEqual(True, b1.id)

    def test_dict(self):
        """test id as a set"""
        b1 = Base()
        b1.id = {4, 5}
        self.assertEqual({4, 5}, b1.id)
