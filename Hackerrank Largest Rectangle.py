#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the largestRectangle function below.
def largestRectangle(h):
    sumi, maxi = 0, 0
    for i in range(len(h)):
        sumi = 0
        for j in range(i, len(h)):
            if h[j] >= h[i]:
                sumi += h[i]
            else:
                break
        for j in range(i-1, -1, -1):
            if h[j] >= h[i]:
                sumi += h[i]
            else:
                break
        maxi = max(maxi, sumi)
    return maxi

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
