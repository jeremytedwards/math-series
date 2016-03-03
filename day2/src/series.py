# -*- coding: utf-8 -*-

import sys

def sum_series(i, a=0, b=1):
    """returns the n-th value of the requested sequence fibonacci or lucas"""
    """defaults to fibonacci sequence"""
    if i == 1:
        return a
    elif i == 2:
        return b
    else:
        for idx in range(i - 2):
            total = a + b
            a = b
            b = total
        return total


# return the 'n' value of the fibonacci sequence
# 0, 1, 1, 2, 3, 5, 8, 13, 21 ....
def fibonacci(n):
    """returns the n-th value of the requested sequence fibonacci sequence"""
    return sum_series(n)


# return the 'n' value of the lucas sequence
# 2, 1, 3, 4, 7, 11, 18, 29 ....
def lucas(n):
    """returns the n-th value of the requested sequence lucas sequence"""
    return sum_series(n, 2, 1)


def main():
    print("This module defines functions that implement mathematical series.")
    print("...\n")

    print("fibonacci(n):\n")

    print("Returns the nth value in the fibonacci series")
    print("0, 1, 1, 2, 3, 5, 8, 13, 21 ....\n")

    print(">>> fibonacci(2)")
    print(fibonacci(2))

    print("\nlucas(n):\n")

    print("Returns the nth value in the lucas series")
    print("2, 1, 3, 4, 7, 11, 18, 29 ....\n")

    print(">>> lucas(2)")
    print(lucas(2))


if __name__ == "__main__":
    sys.exit(main())
