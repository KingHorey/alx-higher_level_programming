#!/usr/bin/python3

def find_peak(list_of_integers):
    """ finds the peak among a list of integers """
    if (list_of_integers is None):
        return None
    if isinstance(list_of_integers, list) is False:
        return None
    if (len(list_of_integers) == 0):
        return None
    if (len(list_of_integers) == 1):
        return list_of_integers[0]
    num = 0
    for i in range(len(list_of_integers)):
        try:
            if (list_of_integers[i] >= list_of_integers[i + 1]):
                num = list_of_integers[i]
        except IndexError:
            pass
    return num
