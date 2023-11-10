#!/usr/bin/python3

def roman_to_int(roman_string):
    """ Function takes arg and calls other relevant functions """
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    else:
        result = num_check(roman_string)
        return result


def num_check(r_str):
    """ performs the calculation for the roman numerals """
    rom_dict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
            }
    calc = 0
    i = 0
    length = len(r_str)
    if length >= 2:
        j = 1
        while i < length:
            try:
                int_1 = rom_dict.get(r_str[i])
                int_2 = rom_dict.get(r_str[j])
                if int_2 and int_1:
                    if int_1 < int_2:
                        result = int_2 - int_1
                    elif int_1 == int_2:
                        result += int_1 + int_2
                    else:
                        result = int_1 + int_2
            except IndexError:
                result = int_1
                calc += result
                break
            calc += result
            result = 0
            if j <= length:
                i = j + 1
                j += 2
    else:
        int_1 = rom_dict.get(r_str)
        calc += int_1
    return calc


if __name__ == "__main__":
    ans = roman_to_int(roman_string)
