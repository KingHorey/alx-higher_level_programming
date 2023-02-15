#!/usr/bin/python3

import unittest
from models.base import *
from models.rectangle import *
from models.square import *
""" Import unittest module to test case"""


class TestBaseID(unittest.TestCase):
    """Unittest cased for base.py"""
    def test_one_args(self):
        """ test instance of Square with one attribute """
        s = Square(3)
        self.assertEqual(Base._Base__nb_objects, s.id)

    def test_instance(self):
        """ test instances where ID is not provided"""
        s = Square(1, 3)
        self.assertEqual(Base._Base__nb_objects, s.id)
    
    def test_two_rec_args(self):
        r = Rectangle(1, 2)
        self.assertEqual(Bae._Base__nb_objects, r.id)

    def test_three_square_args(self):
        s = Square(1, 2, 3)
        self.assertEqual(Base._Base__nb_objects, s.id)

    def test_three_rec_args(self):
        r1 = Rectangle(1, 2, 3)
        self.assertEqual(Base._Base__nb_objects, r1.id)

    def test_four_rec_args(self):
        r1 = Rectangle(1, 3, 5, 2)
        self.assertEqual(Base._Base__nb_objects, r1.id)

    def test_two_rec_args(self):
        r = Rectangle(1, 4)
        self.assertEqual(Base._Base__nb_objects, r.id)

    def test_id_provided(self):
        """ test case when id is provided"""
        r = Rectangle(1, 2, 4, 5, 5)
        s = Square(1, 2, 5, 5)
        self.assertEqual(5, r.id)
        self.assertEqual(5, s.id)

    def test_rect_strings(self):
        """ test instances of rectangle when args is not an int"""

        with self.assertRaises(TypeError):
            r = Rectangle("1", 4)

        with self.assertRaises(TypeError):
            r = Rectangle(1, "4")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 4, "4")

        with self.assertRaises(TypeError):
            r = Rectangle(1, 4, 4, "6")

        with self.assertRaises(ValueError):
            r = Rectangle(0, 4, 3, 6)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 0, 5, 7)

        with self.assertRaises(ValueError):
            r = Rectangle(5, 3, -1, 5)

        with self.assertRaises(ValueError):
            r = Rectangle(1, 4, 0, -4)
    
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

        with self.assertRaises(ValueError):
            r = Square(5, 3, -1)

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

    def test_to_json_rect(self):
        info = Rectangle(1, 3, 4, 5)
        info2 = Rectangle(4, 5, 12, 13)
        info = info.to_dictionary()
        info2 = info2.to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([info])))
        self.assertEqual(str, type(Base.to_json_string([info, info2])))
        self.assertEqual("[]", Base.to_json_string(None))

    def test_to_json_sq(self):
        info = Square(1, 2, 4, 5)
        info2 = Square(2, 3, 1, 8)
        info = info.to_dictionary()
        info2 = info2.to_dictionary()
        self.assertEqual(str, type(Base.to_json_string([info])))
        self.assertEqual(str, type(Base.to_json_string([info])))
        self.assertEqual(str, type(Base.to_json_string([info, info2])))
        self.assertEqual("[]", Base.to_json_string(None))


class test_save_files_square(unittest.TestCase):

    def setUp(self):
        self.s = Square(3, 7, 8, 10)
        self.s2 = Square(4, 6, 1, 8)

    def tearDown(self):
        try:
            os.remove('Square.json')
        except IOError:
            pass

    def test_save_to_json(self):
        Square.save_to_file([self.s])
        with open('Square.json') as f:
            self.assertEqual(len(f.read()), 39)

    def test_save_json_two_obj(self):
        s = Square(2, 3, 5, 3)
        s2 = Square(4, 6, 1, 8)
        Square.save_to_file([self.s2, self.s])
        with open('Square.json') as f:
            self.assertEqual(len(f.read()), 77)


class test_save_files_rectangle(unittest.TestCase):

    def setUp(self):
        self.r = Rectangle(3, 7, 8, 10)
        self.r2 = Rectangle(4, 6, 1, 8)

    def tearDown(self):
        try:
            os.remove('Rectangle.json')
        except IOError:
            pass

    def test_save_to_json(self):
        Rectangle.save_to_file([self.r])
        with open('Rectangle.json') as f:
            self.assertEqual(len(f.read()), 54)

    def test_save_json_two_obj(self):
        Rectangle.save_to_file([self.r2, self.r])
        with open('Rectangle.json') as f:
            self.assertEqual(len(f.read()), 107)


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


class testCreation(unittest.TestCase):
    """ class to test edge caes when new instances
    are created """

    def setUp(self):
        self.r = Rectangle(12, 4)
        self.r1 = Rectangle(13, 5, 1)
        self.s = Square(9, 9, 4)

    def test_create(self):
        r = self.r.to_dictionary()
        r2 = Rectangle.create(**r)
        self.assertEqual(f"[Rectangle] ({self.r.id}) {self.r.x}/{self.r.y} -"
                         f" {self.r.width}/{self.r.height}", str(self.r))
        sq = Square.create(**{'size': 1})
        self.assertEqual(f"[Square] ({sq.id}) {sq.x}/{sq.y} - {sq.size}",
                         str(sq))
        sq = Square(12, 4)
        self.assertEqual(f"[Square] ({sq.id}) {sq.x}/{sq.y} - {sq.size}",
                         str(sq))
        sq = Square(12, 4, 4, 6)
        self.assertEqual(f"[Square] ({sq.id}) {sq.x}/{sq.y} - {sq.size}",
                         str(sq))
        sq = Square(12)
        self.assertEqual(f"[Square] ({sq.id}) {sq.x}/{sq.y} - {sq.size}",
                         str(sq))


if __name__ == "__main__":
    unittest.main()
