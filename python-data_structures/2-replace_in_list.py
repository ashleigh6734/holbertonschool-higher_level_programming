#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position.

    Args:
        my_list (list): List of elements.
        idx (int): Index of the element to replace.
        element (any): New element to insert at index idx.

    Returns:
        The modified list or the original list if idx is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = element
    return my_list
