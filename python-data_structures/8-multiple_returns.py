#!/usr/bin/python3
def multiple_returns(sentence):
    """Return a tuple with the length of a string and its first character.

    Args:
        sentence (str): The string to evaluate.

    Returns:
        tuple: A tuple containing the length of the string and its first character,
               or None if the string is empty.
    """
    if len(sentence) == 0:
        return (0, None)
    else:
        return (len(sentence), sentence[0])
