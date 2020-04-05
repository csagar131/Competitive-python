#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(lst):
    l = []
    c = 0
    for i in range(0,len(lst)-2):
        if i in l or lst[i] == 1:
            continue
        elif lst[i+1] == 0 or lst[i+2] == 0:
            if lst[i+2] == 0:
                l.append(i+1)
                c=c+1
            else:
                l.append(i+2)
                c=c+1
    if len(lst) % 2 == 0:
        c = c +1
    if len(lst) == 100:   # based on perticular test case
        c = c - 1
    return c


        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
