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
    for i,j in a.items():
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





if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
