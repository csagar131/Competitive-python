#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'dynamicArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY queries
#
def  xor(a, b): 
    if a != b: 
        return 1
    else: 
        return 0
    

def dynamicArray(n, queries):
    s0,s1 = [],[]
    lastans = 0
    for i in (queries):
        if(xor(i[1],lastans) % n) ==0:
            s0.append(i[2])
        else:
            lastans = s1[i[2] % len(s1)]
            s1.append(i[2])
            print(lastans)
    print(s0)
    print(s1)


    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    q = int(first_multiple_input[1])

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    result = dynamicArray(n, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
