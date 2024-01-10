#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div

if __name__ == "__main__":
    operator = ""

    if len(sys.argv) != 4:
        print(f"Usage: {sys.argv[0]} <a> <operator> <b>")
        sys.exit(1)
    elif sys.argv[2] not in "+-*/":
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
    else:
        operator = sys.argv[2]
        a, b = int(sys.argv[1]), int(sys.argv[3])

        if operator == '+':
            result = add(a, b)
        elif operator == '-':
            result = sub(a, b)
        elif operator == '*':
            result = mul(a, b)
        else:
            result = div(a, b)

        print(f"{a} {operator} {b} = {result}")
        sys.exit(0)
