#!/usr/bin/python3
def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (any): The value to print.

    Returns:
        True if value has been correctly printed (it means the value is an integer)
        Otherwise, False.
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
