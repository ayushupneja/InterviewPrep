#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maximumToys function below.
def maximumToys(prices, k, n):
   prices.sort()
   runsum = 0
   counter = 0
   print(prices)
   for i in range(n):
       if (prices[i] + runsum) > k:
           return counter
       else:
           runsum += prices[i]
           counter+=1

if __name__ == '__main__':
   fptr = open(os.environ['OUTPUT_PATH'], 'w')

   nk = input().split()

   n = int(nk[0])

   k = int(nk[1])

   prices = list(map(int, input().rstrip().split()))

   result = maximumToys(prices, k, n)

   fptr.write(str(result) + '\n')

   fptr.close()
