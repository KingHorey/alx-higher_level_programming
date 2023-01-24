#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    lgth = sum(1 for i in my_list)
    if (x <= lgth or x < 0):
        i = 0
        counter = 0
        for i in range(x):
            try:
                print("{:d}".format(my_list[i]), end="")
                counter += 1
            except (TypeError, ValueError):
                continue
        print()
        return (counter)
    else:
        raise IndexError
