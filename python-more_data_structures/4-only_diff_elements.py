#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Return a set of all elements present in only one set.

    Args:
        set_1 (set): First set.
        set_2 (set): Second set.

    Returns:
        A set of all elements present in only one set.
    """
    return set_1 ^ set_2
