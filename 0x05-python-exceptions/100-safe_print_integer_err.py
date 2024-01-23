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
        return (True)
    except (TypeError, ValueError):
        print("Exception: {}".format(sys.exc_info()[1]), file=sys.stderr)
        return (False)
