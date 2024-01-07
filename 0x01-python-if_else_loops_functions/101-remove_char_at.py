#!/usr/bin/python3
def remove_char_at(str, n):
    if n < 0 or n > len(str) - 1:
        return str
    str_copy = ""
    for i in range(len(str)):
        if i != n:
            str_copy += str[i]
    return str_copy
