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


class testJsonObj(unittest.TestCase):
    """ class tests the to_json_string in the base class """

    def setUp(self):
        self.s = [{'id': 89, 'width': 10, 'height': 4}]
        self.s1 = [{'id': 89, 'width': 10, 'height': 4}]
        self.s2 = Square(10, 2, 1)
        self.r1 = Rectangle(16, 4, 4)

    def test_one_str(self):
        jsonstr = Base.to_json_string(self.s)
        self.assertEqual(list, type(Base.from_json_string(jsonstr)))

    def test_two_str(self):
        jsonstr = Base.to_json_string([self.s, self.s1])
        self.assertEqual(list, type(Base.from_json_string(jsonstr)))

    def test_empty(self):
        """ test empty list bases as a param"""
        jsonstr = Base.to_json_string([])
        self.assertTrue([] == Base.from_json_string(jsonstr))

    def test_list(self):
        """ create a dict from a list
        convert to a jsonstring and to a python object
        """
        self.s2 = self.s2.to_dictionary()
        jsonst = Base.to_json_string([self.s2])
        self.assertFalse(isinstance(list, type(Base.from_json_string(jsonst))))

    def test_lst_square(self):
        """ return python object from json str """
        self.r1 = self.r1.to_dictionary()
        jsonst = Base.to_json_string([self.r1])
        self.assertFalse(isinstance(list, type(Base.from_json_string(jsonst))))

    def test_few_attr(self):
        s = Square(1, 3)
        r = Rectangle(1, 4)
        s = s.to_dictionary()
        r = r.to_dictionary()
        r_strs = Base.to_json_string([r])
        s_strs = Base.to_json_string([s])
        self.assertFalse(isinstance(list, type(Base.from_json_string(s_strs))))
        self.assertFalse(isinstance(list, type(Base.from_json_string(r_strs))))

    def test_one_args(self):
        """ tests to_json_string when arguments provided
        range from 1"""
        s = Square(1)
        r = Rectangle(4, 5)
        s = s.to_dictionary()
        r = r.to_dictionary()
        r_str = Base.to_json_string([r])
        s_str = Base.to_json_string([s])
        self.assertEqual(list, type(Base.from_json_string(s_str)))
        self.assertEqual(list, type(Base.from_json_string(r_str)))

    def test_none(self):
        self.assertFalse(isinstance(list, type(Base.from_json_string(None))))

    def test_argsOverload(self):
        """ test when more than 1 arg is passed """
        self.s2 = self.s2.to_dictionary()
        with self.assertRaises(TypeError):
            Base.from_json_string([self.s, self.s1], [self.s2])

    def test_argsUnderload(self):
        """ test when more than 1 arg is passed """
        with self.assertRaises(TypeError):
            Base.from_json_string()


class TestSqrCreate(unittest.TestCase):

    def setUp(self):
        self.keys = {'id': 4}
        self.keys1 = {'id': 4, 'size': 6}
        self.keys2 = {'id': 4, 'size': 6, 'x': 3}
        self.keys3 = {'id': 4, 'size': 6, 'x': 3, 'y': 17}

    def test_sqr_create(self):
        s = Square(2)
        s = s.create(**self.keys)
        self.assertEqual(4, s.id)

    def test_sqr_create(self):
        s = Square(2)
        s = s.create(**self.keys1)
        self.assertEqual(4, s.id)

    def test_sqr_create(self):
        s = Square(2)
        s = s.create(**self.keys2)
        self.assertEqual(4, s.id)

    def test_sqr_create(self):
        s = Square(2)
        s = s.create(**self.keys3)
        self.assertEqual(4, s.id)


class TestRecCreate(unittest.TestCase):

    def test_rec_creat(self):
        keys = {'id': 4, 'width': 8, 'height': 9, 'x': 11, 'y': 16}
        r = Rectangle(3, 4)
        r = r.create(**keys)
        self.assertEqual(4, r.id)


class TestSaveFiles(unittest.TestCase):
    """ Class saves to a file """
    def setUp(self):
        try:
            os.remove("Square.json")
        except IOError:
            pass

    def test_none(self):
        Square.save_to_file(None)
        with open("Square.json") as f:
            self.assertEqual(2, len(f.read()))

    def test_none(self):
        Square.save_to_file([])
        with open("Square.json") as f:
            self.assertEqual("[]", f.read())

    def test_one_arg(self):
        s = Square(3)
        Square.save_to_file([s])
        with open("Square.json") as f:
            self.assertEqual(39, len(f.read()))

    def test_two_args(self):
        s = Square(3)
        s1 = Square(4)
        Square.save_to_file([s, s1])
        with open("Square.json") as f:
            self.assertEqual(78, len(f.read()))


class TestSaveFile(unittest.TestCase):
    """ Class saves to a file """

    def test_none(self):
        Rectangle.save_to_file(None)
        with open("Rectangle.json") as f:
            self.assertEqual(str, type(f.read()))

    def test_none(self):
        Rectangle.save_to_file([])
        with open("Rectangle.json") as f:
            self.assertEqual(str, type(f.read()))

    def test_one_arg(self):
        r = Square(3, 2)
        Rectangle.save_to_file([r])
        with open("Rectangle.json") as f:
            self.assertEqual(str, type(f.read()))

    def test_two_args(self):
        r = Rectangle(3, 3, 5, 6)
        r1 = Rectangle(4, 4, 1, 5)
        Square.save_to_file([r, r1])
        with open("Rectangle.json") as f:
            self.assertEqual(str, type(f.read()))


class TestLoadFile(unittest.TestCase):
    """ Test load_from_file """

    def test_none(self):
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]
        Rectangle.save_to_file(list_rectangles_input)
        list_rectangles_output = Rectangle.load_from_file()
        self.assertEqual(list, type(list_rectangles_output))

    def test_one_list(self):
        s = Rectangle(1, 4)
        s1 = Rectangle(2, 3)
        s = Rectangle.load_from_file()
        self.assertEqual([], s)

    def test_empty_list(self):
        self.assertEqual(list, type(Square.load_from_file()))

    def test_one_list(self):
        s = Square.load_from_file()
        self.assertEqual(list, type(s))

    def test_one_list(self):
        s = Square.load_from_file()
        self.assertEqual(list, type(s))

    def test_one_list(self):
        s = Square.load_from_file()
        self.assertEqual(list, type(s))

    def test_one_list(self):
        s = Square(1, 4)
        s1 = Square(2, 3)
        s = Square.save_to_file(None)
        s = Square.load_from_file()
        self.assertEqual(list, type(s))

