#!/usr/bin/python3
import sys

if __name__ == "__main__":
    sum_args = 0
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            sum_args += int(arg)
    print("{:d}".format(sum_args))
