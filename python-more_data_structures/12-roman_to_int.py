#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or not roman_string:
        return 0

    roms = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    num = 0
    for i, x in enumerate(roman_string):
        num += roms[x]
        if i != 0 and roms[roman_string[i-1]] < roms[x]:
            num -= 2 * roms[roman_string[i-1]]

    return num
