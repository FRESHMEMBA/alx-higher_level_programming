#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx in range(len(my_list)):
        temp_list = []
        for i in range(len(my_list)):
            if i != idx:
                temp_list.append(my_list[i])
        my_list = [item for item in temp_list]
    return my_list
