#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """Update a dictionary.

    If `key` exists in `a_dictionary`, its value is updated to `value`.
    If `key` does not exist, it is added to `a_dictionary` with the value `value`.

    Args:
        a_dictionary (dict): The dictionary to update.
        key: The key to add or update.
        value: The value associated with `key`.

    Returns:
        dict: The updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
