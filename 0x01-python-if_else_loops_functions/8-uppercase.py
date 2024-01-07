#!/usr/bin/python3
# def uppercase(str):
#     for c in str:
#         if ord(c) in range(ord('a'), ord('z') + 1):
#             print("{}".format(chr(ord(c) - 32)), end='')
#             continue
#         print("{}".format((c)), end='')
def uppercase(str):
    for c in str:
        print(
            "{}".format(chr(ord(c) - 32))
            if ord(c) in range(ord('a'), ord('z') + 1)
            else c,
            end=''
        )
    print("".format())
uppercase("sergei")