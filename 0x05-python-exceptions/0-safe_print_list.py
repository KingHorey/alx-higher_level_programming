#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if (x > 0):
        try:
            lgth = sum(1 for x in my_list)
            i = 0
            if x >= lgth:
                x = lgth
            while i < x:
                print(my_list[i], end="")
                i += 1
        except IndexError:
            print("Out of bounds")
    print()
    return (i)
