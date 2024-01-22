#!/usr/bin/python3
def safe_print_integer(value):
    """
    Print an integer using "{:d}".format().

    Args:
        value: The value to print.

    Returns:
        True if the value is an integer and has been successfully printed.
        False otherwise.
    """
    try:
        print("{:d}".format(int(value)))
        return True
    except (ValueError, TypeError):
        return False
