#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        lgth = sum(1 for x in my_list)
        i = 0
        if x >= lgth:
            x = lgth
        while i < x:
            if (i == x - 1):
                print("{:s}".format(str(my_list[i])))
            else:
                print("{:s}".format(str(my_list[i])), end="")
            i += 1
    except (len(my_list) == 0):
        print("Empty list")
    return (i)
