#!/usr/bin/python3

import unittest
from models.base import *
from models.rectangle import *
from models.square import *


class Test_sqr_id(unittest.TestCase):
    """ Test id attribute for Square instances"""

    def test_none(self):
        """ Test id for Square when None """
        s = Square(1, 2)
        self.assertEqual(Base._Base__nb_objects, s.id)

    def test_int_id(self):
        """ test id when an int """
        s = Square(1, 2, 3, 4)
        self.assertEqual(4, s.id)

    def test_str_id(self):
        """ Test id when a string """
        s = Square(1, 2, 3, "4")
        self.assertEqual("4", s.id)

    def test_dict_id(self):
        """ Test id when a dict """
        s = Square(1, 2, 3, {'x': 4, 'y': 5})
        self.assertEqual({'x': 4, 'y': 5}, {'x': 4, 'y': 5})

    def test_tuple_id(self):
        """ test Square id when it is a tuple """
        s = Square(1, 2, 3, (4, 5))
        self.assertEqual((4, 5), s.id)

    def test_list_id(self):
        """ Test id when it is a list """
        s = Square(1, 2, 3, [5, 6])
        self.assertEqual([5, 6], s.id)

    def test_set_id(self):
        """ Test id when it is a set """
        s = Square(1, 2, 3, {5, 6})
        self.assertEqual({5, 6}, {5, 6})


class TestSetters(unittest.TestCase):
    """ This class tests the gettes.and settes.functions that
        are in the Square class

        Errors:
        ValueErros.is raised when:
        1. size is under or equals to Zero
        2. x or y is lesser than Zero

        TypeError:
        1. size or height is not an integer
        2. x or y is not an integer
    """

    def test_size(self):
        """ test when size is a string and also when less than 0"""
        with self.assertRaises(TypeError):
            s = Square("1", 2)

        with self.assertRaises(ValueError):
            s = Square(0, 2)

        with self.assertRaises(ValueError):
            s = Square(-1, 2)

    def test_x(self):
        """ test when height is a string """
        with self.assertRaises(TypeError):
            s = Square(1, "2")

        with self.assertRaises(ValueError):
            s = Square(1, -1)

        with self.assertRaises(TypeError):
            s = Square(1, [3, 4], 5)

        with self.assertRaises(TypeError):
            s = Square(1, (3, 4), 5)

        with self.assertRaises(TypeError):
            s = Square(1, {3, 4}, 5)

        with self.assertRaises(TypeError):
            s = Square(1, {'x': 3, 'y': 4}, 5)

    def test_y(self):
        """ test when x is not an integer."""
        with self.assertRaises(TypeError):
            s = Square(1, 2, "3")

        with self.assertRaises(ValueError):
            s = Square(1, 0, -1)

        with self.assertRaises(TypeError):
            s = Square(1, 2, [3, 4], 5)

        with self.assertRaises(TypeError):
            s = Square(1, 2, (3, 4), 5)

        with self.assertRaises(TypeError):
            s = Square(1, 2, {3, 4}, 5)

        with self.assertRaises(TypeError):
            s = Square(1, 2, {'x': 3, 'y': 4}, 5)


class TestArea(unittest.TestCase):
    """ Class tests the area() method """

    def test_int(self):
        s = Square(2)
        self.assertAlmostEqual(4, s.area())


class TestUpdateArgs(unittest.TestCase):
    """ This class tests update(*args, **kwargs)"""

    def testargsWH(self):
        """ This method tests the update method on size
        and height
        """
        s = Square(1, 2)
        s.update(3, 4)
        self.assertEqual(4, s.size)

    def testargsX(self):
        s = Square(1, 2, 3)
        s.update(4, 5, 6)
        self.assertEqual(6, s.x)

    def testargsY(self):
        s = Square(1, 2, 3, 4)
        s.update(5, 6, 7, 8)
        self.assertEqual(8, s.y)

    def test_full_args(self):
        """ Tests all args """
        s = Square(1, 2, 3, 4)
        s.update(6, 7, 8, 9)
        self.assertEqual(s.id, 6)


class TestKwargs(unittest.TestCase):
    """ This class tests kwargs in replacing attributes of an instance"""

    def setUp(self):
        self.s = Square(1, 2)
        self.dicts0 = {'size': 2}
        self.dicts1 = {'size': 2, 'height': 5, 'x': 15}
        self.dicts2 = {'size': 2, 'height': 5, 'x': 15, 'y': 20}
        self.dicts3 = {'size': 2, 'height': 5, 'x': 15, 'y': 20, 'id': 15}

    def tearDown(self):
        """ Deletes the class objects after test calls"""
        del self.s

    def testsizekwargs(self):
        """ This method update the values in the object by
        the values in the dict """

        self.s.update(**self.dicts0)
        self.assertEqual(2, self.s.size)

    def testheightkwargs(self):
        """ This method update the values in the object by
        the values in the dict """

        self.s.update(**self.dicts1)
        self.assertEqual(5, self.s.height)

    def testXkwargs(self):
        """ Test kwargs update for x """
        self.s.update(**self.dicts1)
        self.assertEqual(15, self.s.x)

    def testYkwargs(self):
        """ Test kwargs update for height """
        self.s.update(**self.dicts2)
        self.assertEqual(20, self.s.y)

    def test_id_kwargs(self):
        """ Test kwargs update for id """
        self.s.update(**self.dicts3)
        self.assertEqual(15, self.s.id)


class TestToJson(unittest.TestCase):

    def test_to_json_rect(self):
        """ Create a json file when one list is passed """

        info = Square(1, 3, 4, 5)
        info = info.to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([info])))

    def test_to_json_rect1(self):
        """ Create a json file when two lists are passed """
        info = Square(1, 3, 4, 5)
        info2 = Square(4, 5, 12, 13)
        info = info.to_dictionary()
        info2 = info2.to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([info, info2])))

    def test_to_json_none(self):
        """ Test when list_dictionaries is none """
        self.assertEqual("[]", Base.to_json_string(None))
