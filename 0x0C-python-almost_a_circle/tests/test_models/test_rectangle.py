#!/usr/bin/python3

import unittest
from models.base import *
from models.rectangle import *
from models.square import *
from io import StringIO
import sys


class Test_rec_id(unittest.TestCase):
    """ Test id attribute for Rectangle instances"""

    def test_none(self):
        """ Test id for rec when None """
        r = Rectangle(1, 2)
        self.assertEqual(Base._Base__nb_objects, r.id)

    def test_int_id(self):
        """ test id when an int """
        r = Rectangle(1, 2, 3, 4, 5)
        self.assertEqual(5, r.id)

    def test_str_id(self):
        """ Test id when a string """
        r = Rectangle(1, 2, 3, 4, "5")
        self.assertEqual("5", r.id)

    def test_dict_id(self):
        """ Test id when a dict """
        r = Rectangle(1, 2, 3, 4, {'x': 4, 'y': 5})
        self.assertEqual({'x': 4, 'y': 5}, {'x': 4, 'y': 5})

    def test_tuple_id(self):
        """ test rectangle id when it is a tuple """
        r = Rectangle(1, 2, 3, 4, (4, 5))
        self.assertEqual((4, 5), r.id)

    def test_list_id(self):
        """ Test id when it is a list """
        r = Rectangle(1, 2, 3, 4, [5, 6])
        self.assertEqual([5, 6], r.id)

    def test_set_id(self):
        """ Test id when it is a set """
        r = Rectangle(1, 2, 3, 4, {5, 6})
        self.assertEqual({5, 6}, {5, 6})


class TestSetters(unittest.TestCase):
    """ This class tests the getter and setter functions that
        are in the Rectangle class

        Errors:
        ValueError is raised when:
        1. width or height is under or equals to Zero
        2. x or y is lesser than Zero

        TypeError:
        1. width or height is not an integer
        2. x or y is not an integer
    """

    def test_width(self):
        """ test when width is a string """
        with self.assertRaises(TypeError):
            r = Rectangle("1", 2)

        with self.assertRaises(ValueError):
            r = Rectangle(0, 1)

        with self.assertRaises(ValueError):
            r = Rectangle(-2, 3)

    def test_height(self):
        """ test when height is a string """
        with self.assertRaises(TypeError):
            r = Rectangle(1, "2")

        with self.assertRaises(ValueError):
            r = Rectangle(1, 0)

        with self.assertRaises(ValueError):
            r = Rectangle(1, -1)

    def test_x(self):
        """ test when x is not an integer """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, "3")

        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, -3)

    def test_y(self):
        """ Test when y is not an integer """
        with self.assertRaises(TypeError):
            r = Rectangle(1, 2, 3, "4")

        with self.assertRaises(ValueError):
            r = Rectangle(1, 2, 3, -4)


class TestArea(unittest.TestCase):
    """ Class tests the area() method """

    def test_int(self):
        s = Rectangle(2, 3)
        self.assertAlmostEqual(6, s.area())


class Test_str_(unittest.TestCase):
    """ Test the __str__ method """

    def setUp(self):
        """ Create Rectangle instances """
        self.r = Rectangle(4, 6)
        self.r1 = Rectangle(4, 6, 2)
        self.r2 = Rectangle(4, 6, 2, 1)

    def testone(self):
        """ Test the count of __str__ """
        self.assertEqual(f"[Rectangle] ({self.r.id}) {self.r.x}/"
                         f"{self.r.y} - {self.r.width}/{self.r.height}",
                         self.r.__str__())

    def testone(self):
        """ Test the count of __str__ """
        self.assertEqual(f"[Rectangle] ({self.r1.id}) {self.r1.x}/"
                         f"{self.r1.y} - {self.r1.width}/{self.r1.height}",
                         self.r1.__str__())

    def testone(self):
        """ Test the count of __str__ """
        self.assertEqual(f"[Rectangle] ({self.r2.id}) {self.r2.x}/"
                         f"{self.r2.y} - {self.r2.width}/{self.r2.height}",
                         self.r2.__str__())


class TestUpdateArgs(unittest.TestCase):
    """ This class tests update(*args, **kwargs)
    ["id", "width", "height", "x", y]
    """
    def testargsWH(self):
        """ This method tests the update method on width
        and height
        """
        r = Rectangle(1, 2)
        r.update(3, 4, 5)
        self.assertEqual(4, r.width)
        self.assertEqual(5, r.height)

    def testargsX(self):
        r = Rectangle(1, 2, 3, 4)
        r.update(4, 5, 6, 7)
        self.assertEqual(7, r.x)

    def testargsY(self):
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(5, 6, 7, 8, 9)
        self.assertEqual(9, r.y)

    def test_full_args(self):
        """ Tests all args """
        r = Rectangle(1, 2, 3, 4, 5)
        r.update(6, 7, 8, 9, 10)
        self.assertEqual(6, r.id)


class TestKwargs(unittest.TestCase):
    """ This class tests kwargs in replacing attributes of an instance"""

    def setUp(self):
        self.r = Rectangle(1, 2)
        self.dicts0 = {'width': 2, 'height': 5}
        self.dicts1 = {'width': 2, 'height': 5, 'x': 15}
        self.dicts2 = {'width': 2, 'height': 5, 'x': 15, 'y': 20}
        self.dicts3 = {'width': 2, 'height': 5, 'x': 15, 'y': 20, 'id': 15}

    def tearDown(self):
        """ Deletes the class objects after test calls"""
        del self.r

    def testwidthkwargs(self):
        """ This method update the values in the object by
        the values in the dict """

        self.r.update(**self.dicts0)
        self.assertEqual(2, self.r.width)

    def testheightkwargs(self):
        """ This method update the values in the object by
        the values in the dict """

        self.r.update(**self.dicts0)
        self.assertEqual(5, self.r.height)

    def testXkwargs(self):
        """ Test kwargs update for x """
        self.r.update(**self.dicts1)
        self.assertEqual(15, self.r.x)

    def testYkwargs(self):
        """ Test kwargs update for height """
        self.r.update(**self.dicts2)
        self.assertEqual(20, self.r.y)

    def test_id_kwargs(self):
        """ Test kwargs update for x """
        self.r.update(**self.dicts3)
        self.assertEqual(15, self.r.id)


class TestDisplay(unittest.TestCase):
    """ Test display method """

    tmp = sys.stdout
    store = StringIO()
    sys.stdout = store

    def setUp(self):
        self.r = Rectangle(1, 2)
        self.r1 = Rectangle(3, 2, 3)
        self.r2 = Rectangle(3, 2, 2, 2)
        self.r3 = Rectangle(7, 2, 3, 4, 5)

    def test_out(self):
        print(self.r.display())
        if self.r.y == 0:
            self.assertEqual("#\n#\n", TestDisplay.store.getvalue())

    def test_out(self):
        print(self.r1.display())
        x = "   ###\n   ###\nNone\n"
        self.assertEqual(x, TestDisplay.store.getvalue())

    def test_out(self):
        print(self.r2.display())
        x = ""
        for i in range(self.r2.y):
            x += ""
            x += "\n"
        for i in range(self.r2.height):
            x += " "*self.r2.x + "#" * self.r2.width
            x += "\n"
        x += "None\n"
        self.assertEqual(x, TestDisplay.store.getvalue())


class TestToJson(unittest.TestCase):
    """ Class tests creating a json string
        Relevant information:
        to_json_string makes use of .to_dictionary() to convert
        python object into a serializable  object
    """

    def test_to_json_rect(self):
        info = Rectangle(1, 3, 4, 5)
        info = info.to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([info])))

    def test_to_json_rect1(self):
        info = Rectangle(1, 3, 4, 5)
        info2 = Rectangle(4, 5, 12, 13)
        info = info.to_dictionary()
        info2 = info2.to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([info, info2])))

    def test_to_json_rect1(self):
        info = Rectangle(1, 3, 4, 5, 6)
        info2 = Rectangle(4, 5, 12, 13, 15)
        info = info.to_dictionary()
        info2 = info2.to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([info, info2])))

    def test_to_json_none(self):
        """ Test when list_dictionaries is none """
        self.assertEqual("[]", Base.to_json_string(None))
