#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the repeatedString function below.
def repeatedString(s, n):
    a_cnt = s.count('a')
    num = n//len(s)
    mod = n%len(s)
    count = a_cnt*num + s[:mod].count('a')
    return count 
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
