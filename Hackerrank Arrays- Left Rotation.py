#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def left_shift(n,k,a):
   for _ in range(k):
      a.append(a.pop(0))
   return a



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = left_shift(n,d,a)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
