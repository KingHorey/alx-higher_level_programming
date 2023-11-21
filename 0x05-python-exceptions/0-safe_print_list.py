#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    if my_list is not None:
        lgth = sum(1 for _ in my_list)
    if (x >= 0):
        try:
            i = 0
            if x >= lgth:
                x = lgth
            while i <= x:
                print(my_list[i], end="")
                i += 1
            print()
            return(i)
        except IndexError:
            return (0)
    else:
        y = -(lgth)
        count = 0
        while x >= y:
            print(my_list[x], end="")
            x -= 1
            count += 1
        print()
        return (count)
