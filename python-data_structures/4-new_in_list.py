#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    """Replaces an element in a list at a specific position without modifying
    the original list.

    Args:
        my_list (list): List of elements.
        idx (int): Index of the element to replace.
        element (any): New element to insert at index idx.

    Returns:
        A new list with the modified element or a copy of the original list
        if idx is out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
