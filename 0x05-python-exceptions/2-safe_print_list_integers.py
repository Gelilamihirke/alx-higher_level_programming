#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print the first x integer elements from a list.

    Args:
        my_list (list): The list to print elements from.
        x (int): The number of elements of my_list to print.

    Returns:
        The number of integers printed.
    """
    count = 0
    try:
        for i in range(x):
            try:
                if isinstance(my_list[i], int):
                    print("{:d}".format(my_list[i]), end="")
                    count += 1
            except (IndexError, ValueError, TypeError):
                pass
    finally:
        print()
        return count
