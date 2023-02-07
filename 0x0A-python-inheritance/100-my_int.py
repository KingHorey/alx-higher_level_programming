#!/usr/bin/python3

"""NO modules imported"""


class MyInt(int):
    """ My int is an opposite of int and has
    == and != inverted """

    def __eq__(self, int):
        return False

    def __ne__(self, int):
        return True
