#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the stepPerms function below.
#def stepPerms(n):
#    if n == 0:
#        return 0
#    if n == 1:
#        return 1
#    if n == 2:
#        return 2
#    if n == 3:
#        return 4
#    return (stepPerms(n-1) + stepPerms(n-2) + stepPerms(n-3))% 10000000007

def stepPerms(n):
    dp ={}
    dp[1],dp[2],dp[3] = 1,2,4
    for i in range(4,n+1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    return dp[n]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = int(input())

    for s_itr in range(s):
        n = int(input())

        res = stepPerms(n)

        fptr.write(str(res) + '\n')

    fptr.close()
