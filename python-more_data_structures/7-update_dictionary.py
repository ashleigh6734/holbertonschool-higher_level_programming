#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    """
    Replace or add a key/value pair in a dictionary.

    :param a_dictionary: dict - the dictionary to update.
    :param key: str - the key to update or add.
    :param value: any - the value to assign to the key.
    :return: dict - the updated dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
