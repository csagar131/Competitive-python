#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the migratoryBirds function below.
def migratoryBirds(arr):
    arr.sort()
    print(arr)
    mx = max(arr)
    freq = []
    for i in range(0,mx+1):
        freq.append(0)
    #print(freq)
    for i in range(0,len(arr)):
        k = arr[i]
        freq[k] = freq[k] + 1
    
    #print(freq)
    for i in range(0,len(freq)):
        if freq[i] == max(freq):
            return i

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
