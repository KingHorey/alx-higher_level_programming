#!/usr/bin/python3

"""No modules imported"""


class Rectangle:
    """This class receives dimensions for a rectangle
    and returns the perimeter"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def height(self):
        """Returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets the value if height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets the value of width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        return (2 * (self.__width + self.__height))

    def __str__(self):
        """returns a formal string representation of the object"""
        output = ""
        for i in range(self.__height):
            output += "#" * self.__width + "\n"
        return (output.rstrip())

    def __repr__(self):
        """returns a formal string representation which
        can be used to creat other instances"""
        return "Rectangle({:d}, {:d})".format(self.__width, self.__height)
