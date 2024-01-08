#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    cur = my_list[:]
    if idx < 0:
        return cur
    if idx > len(my_list) - 1:
        return cur
    cur[idx] = element
    return cur
