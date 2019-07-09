#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    stack = []
    b = 1
    for i in range(len(s)):
        if (s[i] == "{" or s[i] == "[" or s[i] == "("):
            stack.append(s[i])
        else:
            if stack:
                a = stack.pop()
                if s[i] == "]":
                    if a != "[":
                        b = 0
                if s[i] == "}":
                    if a != "{":
                        b = 0
                if s[i] == ")":
                    if a != "(":
                        b = 0
            else:
                b = 0
    if stack:
        b = 0
    if b == 1:
        return("YES")
    else:
        return("NO")



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
