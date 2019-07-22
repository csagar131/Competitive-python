#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    mx =0
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            count = 9
            sum1 = 0
            for k in range(i,i+3):
                for l in range(j,j+3):
                    if count is not 4 and count is not 6: 
                        sum1 = sum1 + arr[k][l]
                        #print(arr[k][l],end="")  debugging purpose
                        count = count - 1
                    else:
                        count = count - 1
                #print()   debugging purposes
            if sum1 > mx:
                mx = sum1
    return mx

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
