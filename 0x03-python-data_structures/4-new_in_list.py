#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    copy_list = []
    for item in my_list:
        copy_list.append(item)
    if idx in range(len(my_list)):
        copy_list[idx] = element
    return copy_list
