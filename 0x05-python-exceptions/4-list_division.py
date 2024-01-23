#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divide corresponding elements of two lists element-wise.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The desired length of the resulting list.

    Returns:
        A new list with the division results.

    """
    n_list = []
    for i in range(list_length):
        try:
            div = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            div = 0
        except ZeroDivisionError:
            print("division by 0")
            div = 0
        except IndexError:
            print("out of range")
            div = 0
        finally:
            n_list.append(div)
    return n_list
