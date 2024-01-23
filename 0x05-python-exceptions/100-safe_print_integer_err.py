#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """
    Print an integer value.

    Args:
        value: The value to be printed.

    Returns:
        True if the value is an integer and successfully printed.
        False otherwise.

    """
    try:
        print("{:d}".format(value))
    except (ValueError, TypeError) as err:
        print("Exception: {}".format(err), file=sys.stderr)
        return False
    else:
        return True
