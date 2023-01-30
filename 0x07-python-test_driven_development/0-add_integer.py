#!/usr/bin/python3

"""No modules imported"""


def add_integer(a, b=98):
    """ function returns the addition of two integers
    Args:
        a(float or int): A number representing the first add_integer in the addition
        b(float or int): A number representing the first add_integer in the addition. B has a default value of 98
    Returns:
        The addition of an integer
    
    Raises:
        TypeError if a or b is not an intger nor a float or if a is not provided
    """
    if isinstance(a, (int,float)) is False or a is None:
        raise TypeError("a must be an integer")
    if isinstance(b, (int, float)) is False:
        raise TypeError("b must be an integer")
    if isinstance(a, float):
        a = int(a)
    if isinstance(b, float):
        b = int(b)
    return (a + b)

