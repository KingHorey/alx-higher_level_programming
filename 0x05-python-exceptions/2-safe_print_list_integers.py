#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    if my_list is not None:
        """
        get the length of the list
        """
        lgth = sum(1 for i in my_list)
        count = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                count += 1
            except ValueError:
                continue
            except TypeError:
                continue
        print()
        return (count)
    else:
        raise IndexError
