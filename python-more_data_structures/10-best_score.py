#!/usr/bin/python3
def best_score(a_dictionary):
    """Return the key with the highest value in a dictionary.

    If `a_dictionary` is empty, return `None`.

    Args:
        a_dictionary (dict): The dictionary to evaluate.

    Returns:
        The key with the highest value, or `None` if the dictionary is empty.
    """
    if not a_dictionary:
        return None
    return max(a_dictionary, key=a_dictionary.get)
