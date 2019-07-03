#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    issorted = False
    swaps = 0

    while not issorted:
        issorted = True
        for i in range(0, len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                swaps += 1
                issorted = False

    print("Array is sorted in %d swaps." % swaps)
    print("First Element: %d" % a[0])
    print("Last Element: %d" % a[-1])

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
