#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    lst = []
    for i in range(0,len(ar)-1):
        for j in range(i+1,len(ar)):
            if i in lst or j in lst:
                continue
            else:
                if ar[i] == ar[j]:
                    lst.append(i)
                    lst.append(j)
    return len(lst)//2




if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
