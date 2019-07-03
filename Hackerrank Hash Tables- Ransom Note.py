#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    counter = 0
    if len(magazine) < len(note):
        print("No")
        return 0
    magazine.sort()
    note.sort()
    for i in range(len(note)):
        if note[i] in magazine:
            counter+=1
            magazine.remove(note[i])
        else:
            print("No")
            break
    if counter == len(note):
        print("Yes")


if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
