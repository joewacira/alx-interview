#!/usr/bin/python3
""" Module for 0-minoperations"""


def minOperations(n):
    """
    minOperations
    Gets fewest # of operations needed to result in exactly n H characters
    """
    # all the outputs should be atleast (2) char: (min, Copy All => Paste)
    if (n < 2):
        return 0
    ops, root = 0, 2
    while root <= n:
        # if n evenly divides by root
        if n % root == 0:
            # total even-divisions by root = total_operations
            ops += root
            # set n to remainder
            n = n / root
            # reduce the root to find remaining smaller vals that evenly-divide n
            root -= 1
        # increment the root until it evenly-divides n
        root += 1
    return ops

