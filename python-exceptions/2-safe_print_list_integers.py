#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """Print x elements of a list that are integers.

    Args:
        my_list (list): List of elements.
        x (int): Number of elements to print.

    Returns:
        The real number of integers printed.
    """
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (ValueError, TypeError):
            continue
        except IndexError:
            break
    print()
    return count