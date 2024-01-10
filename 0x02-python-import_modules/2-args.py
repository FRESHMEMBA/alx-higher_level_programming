#!/usr/bin/python3
import sys

if __name__ == "__main__":
    n_args = len(sys.argv) - 1
    if n_args == 0:
        print(f"{n_args} arguments.")
    else:
        if n_args == 1:
            print(f"{n_args} argument:")
        else:
            print(f"{n_args} arguments:")
        for i in range(1, len(sys.argv)):
            print(f"{i}: {sys.argv[i]}")

