#!/usr/bin/python3
def max_integer(my_list=[]):
    """Find the biggest integer in a list.

    Args:
        my_list (list): List of integers.

    Returns:
        The biggest integer or None if the list is empty.
    """
    if not my_list:
        return None
    max_value = my_list[0]
    for num in my_list:
        if num > max_value:
            max_value = num
    return max_value
