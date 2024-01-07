#!/usr/bin/python3
for char in range(ord('z'), ord('a') - 1, -1):
    print(
        "{}".format(chr(char)) if char % 2 == 0
        else "{}".format(chr(char - 32)),
        end=''
    )
