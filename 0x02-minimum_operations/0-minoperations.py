#!/usr/bin/python3
'''Minimum Operations python3 challenge'''


def minOperations(n):
    '''calculates the fewest number of
    operations needed to result in exactly n H
    characters in this file.
    Returns:
        Integer : if n is impossible to achieve, return 0
    '''
    pastedChars = 1  # how many chars in the file
    copied = 0  # how many H's copied
    counter = 0  # operations counter

    while pastedChars < n:
        # if did not copy anything yet
        if copied == 0:
            # copyall
            copied = pastedChars
            # increment operations counter
            counter += 1

        # if haven't pasted anything yet
        if pastedChars == 1:
            # paste
            pastedChars += copied
            # increment operations counter
            counter += 1
            # continue to next loop
            continue

        remaining = n - pastedChars  # remaining chars to Paste
        # check if impossible by checking if copied
        # has more than needed to reach the number desired
        # which also means num of chars in file is equal
        # or more than in the copied.
        # in both situations it's impossible to achieve n of chars
        if remaining < copied:
            return 0

        # if can't be devided
        if remaining % pastedChars != 0:
            # paste current copied
            pastedChars += copied
            # increment operations counter
            counter += 1
        else:
            # copyall
            copied = pastedChars
            # paste
            pastedChars += copied
            # increment operations counter
            counter += 2

    # if got the desired result
    if pastedChars == n:
        return counter
    else:
        return 0