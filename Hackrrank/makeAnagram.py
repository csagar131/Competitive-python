#!/bin/python3
from collections import Counter
import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a = dict(Counter(list(a)))
    b = dict(Counter(list(b)))
    c = 0
    print(a)
    print(b)
    for i,j in a.items():      # method is taking too long to execute
        if i  not in b.keys():
            c = c + a.get(i)
        else:
            if b.get(i) > a.get(i):
                while b.get(i) is not a.get(i):
                    b[i] = b.get(i)-1
                    c = c + 1
            else:
                while a.get(i) is not b.get(i):
                    a[i] = a.get(i) - 1
                    c = c + 1
    else:
        for i,j in b.items():
            if i not in a.keys():
                c = c + b.get(i)
    return c

'''
from math import fabs

def number_needed(a, b):
    letterArray = [0] * 26
    for c in a:
        index = ord(c) - ord('a');
        letterArray[index]+=1
    for c in b:
        index = ord(c) - ord('a')
        letterArray[index]-=1
    result = 0
    for i in letterArray:
        result += fabs(i)
    return int(result)
    
a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)

'''



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
