#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_numbers = set(my_list)
    sum_of_unique = 0

    for number in unique_numbers:
        sum_of_unique += number

    return (sum_of_unique)
