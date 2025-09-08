#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list.

    Args:
        my_list (list): List of integers.

    Returns:
        A list of boolean values representing whether each integer is
        a multiple of 2.
    """
    return [num % 2 == 0 for num in my_list]
    # Alternatively, using a for loop:
    # result = []
    # for num in my_list:
    #     result.append(num % 2 == 0)
    # return result 
