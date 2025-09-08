#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples.

    Args:
        tuple_a (tuple): First tuple.
        tuple_b (tuple): Second tuple.

    Returns:
        tuple: A new tuple with the sum of the two tuples.
    """
    a1, a2 = (tuple_a + (0, 0))[:2]
    b1, b2 = (tuple_b + (0, 0))[:2]
    return (a1 + b1, a2 + b2)
