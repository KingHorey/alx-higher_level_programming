#!/usr/bin/python3

"""No modules imported"""


class MyList(list):
    """ This class inherits from parent class list and
    performs operation """
    def print_sorted(self):
        """ prints sorted list in ascending order """
        print(sorted(self))
