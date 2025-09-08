#!/usr/bin/python3
def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral to convert.

    Returns:
        int: The integer representation of the Roman numeral.
    """
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    for char in reversed(roman_string):
        if char not in roman_numerals:
            return 0
        value = roman_numerals[char]
        if value < prev_value:
            total -= value
        else:
            total += value
        prev_value = value

    return total
