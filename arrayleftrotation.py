from collections import deque
#!/bin/python3

import math
import os
import random
import re
import sys


def left_rotate(arr,d):
    lst = deque()
    for i in arr:
        lst.append(i)
    lst.rotate(-d)
    return list(lst)

'''
// Shift elements from indices d through n to indices 0 through d - 1:
        for(int i = d; i < n; i++) {
            arr[i - d] = arr[i];
        }
        
        // Copy the d shifted elements from the temporary array back to thearray:
        for(int i = n - d; i < n; i++) {
            arr[i] = temp_arr[i-n+d];
'''
    

if __name__ == '__main__':
    nd = input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = list(map(int, input().rstrip().split()))

    result = left_rotate(a,d)

    for i in result:
        print(i,end=' ')



