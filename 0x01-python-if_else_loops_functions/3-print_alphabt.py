#!/usr/bin/python3
for char in range(ord('a'), ord('z') + 1):
    if chr(char) in "eq":
        continue
    else:
        print("{}".format(chr(char)), end='')

