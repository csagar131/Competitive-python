#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            count = 0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    print(arr[k][l],end=' ')

            

        print()

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
