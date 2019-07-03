#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):

    dict={}
    count=0
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            list1= list(s[i:j].strip())
            list1.sort()
            transf=''.join(list1)
            if transf in dict:
                count+=dict[transf]
                dict[transf]=dict[transf]+1
            else: dict[transf]=1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
