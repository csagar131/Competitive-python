#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    x = s
    y = t
    t = list(t)
    s = list(s)
    count = 0
    if s==t:
        l = len(t)
        rem = k-l 
        for i in range(0,rem):
            if len(t) is not 0:
                t.remove(t[len(t)-1])
                count = count +1
            else:
                count = count + 1
        for i in range(0,len(s)):
            t.append(s[i])
            count = count + 1
        if count is k:
            return 'Yes'
        else:
            return 'No'
    elif x.find(y) is not -1:
        s = list(x)
        t = list(y)
        m = len(s) - len(t)
        for i in range(0,m):
            s.remove(s[len(s)-1])
            count = count + 1
        if count is k:
            return 'Yes'
        else:
            return 'No'

        #print("need to work on this case")

    else:
        for i in range(0,len(s)):
            if s[i] is not t[i]:
                m = i
                break
        rem = len(s) - m
        for i in range(0,rem):
            s.remove(s[len(s)-1])
            count = count +1
        for i in range(m,len(t)):
            s.append(t[i])
            count = count + 1
        print(count)
        if count is k:
            return 'Yes'
        else:
            return 'No'
        

    



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

    fptr.write(result + '\n')

    fptr.close()
