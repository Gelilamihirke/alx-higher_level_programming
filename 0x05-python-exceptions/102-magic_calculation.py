#!/usr/bin/python5
def magic_calculation(a, b):
    """
    Perform a magic calculation using the inputs a and b.

    Args:
        a (int): The first input.
        b (int): The second input.

    Returns:
        The result of the magic calculation.

    """
    result = 0
    for i in range(1, 3):
        try:
            if i > a:
                raise ValueError('Too far')
            result += a ** b / i
        except ValueError:
            result = b + a
            break
    return result
