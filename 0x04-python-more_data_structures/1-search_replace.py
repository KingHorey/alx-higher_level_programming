#!/usr/bin/python3
def search_replace(my_list, search, replace):
    if not my_list:
        return my_list
    else:
        new_list = my_list.copy()
        result = map(lambda x: replace if x == search else x, new_list)

        return (list(result))
