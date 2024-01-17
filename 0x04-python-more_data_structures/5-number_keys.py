#!/usr/bin/python3
def number_keys(a_dictionary):
    key_count = 0
    keys_list = list(a_dictionary.keys())

    for key in keys_list:
        key_count += 1

    return key_count
