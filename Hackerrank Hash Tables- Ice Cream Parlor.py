#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the whatFlavors function below.
def whatFlavors(cost, money):
    oldVals = {}
    for i, c in enumerate(cost, start=1):
        diff = money - c
        prev = oldVals.get(diff, -1)
        if(prev == -1):
            oldVals[c] = i
        else:
            print(str(prev) + " " + str(i))
if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        money = int(input())

        n = int(input())

        cost = list(map(int, input().rstrip().split()))

        whatFlavors(cost, money)
s
