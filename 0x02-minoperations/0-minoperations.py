#!/usr/bin/python3

"""
    calculates the fewest number of operations needed to
    result in exactly n H characters in the file
"""


def minOperations(n):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        Return: fewest number of operations
    """

    current = 1
    start = 0
    counter = 0
    while current < n:
        remainder = n - current
        if (remainder % current == 0):
            start = current
            current += start
            counter += 2
        else:
            current += start
            counter += 1
    return counter
