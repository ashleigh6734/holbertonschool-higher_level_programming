#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    """Delete a key in a dictionary.

    If `key` is in `a_dictionary`, it is deleted. Otherwise, the dictionary
    remains unchanged.

    Args:
        a_dictionary (dict): The dictionary to modify.
        key: The key to delete.

    Returns:
        dict: The modified dictionary.
    """
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
