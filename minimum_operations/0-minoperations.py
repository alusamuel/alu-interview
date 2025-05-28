#!/usr/bin/python3
"""
Module that calculates the fewest number of operations
"""


def minOperations(n):
    """
    Calculate the minimum number of operations required to achieve
    exactly n 'H' characters in a text file using only two operations:
    Copy All and Paste.

    The function works by finding the prime factors of n and summing them,
    which reflects the optimal sequence of copy-paste operations.

    Parameters:
        n (int): The target number of 'H' characters.

    Returns:
        int: The minimum number of operations required. Returns 0 if n < 2.
    """
    if n < 2:
        return 0

    operations = 0
    divisor = 2

    while n > 1:
        # If n is divisible by the current divisor, divide n and
        # add the divisor to the operations count. Repeat until it isn't.
        while n % divisor == 0:
            operations += divisor
            n //= divisor
        divisor += 1

    return operations
