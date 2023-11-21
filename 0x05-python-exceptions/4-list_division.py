#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for x in range(list_length):
        try:
            ans = my_list_1[x] / my_list_2[x]
        except ZeroDivisionError:
            print("division by 0")
            ans = 0
        except (ValueError, TypeError):
            print("wrong type")
            ans = 0
        except IndexError:
            print("out of range")
            ans = 0
        finally:
            new_list.append(ans)
    return (new_list)
