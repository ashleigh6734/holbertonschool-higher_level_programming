#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Print x elements of a list.

    Args:
        my_list (list): List of elements.
        x (int): Number of elements to print.

    Returns:
        The real number of elements printed.
    """
    count = 0
    for i in range(x):
        try:
            print(my_list[i], end="")
            count += 1
        except IndexError:
            break
    print()
    return count
