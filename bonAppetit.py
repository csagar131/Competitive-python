#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    sum1 = 0
    for i in range(0,len(bill)):
        if bill[i] is not bill[k]:
            sum1= sum1 + bill[i]
    k = sum1//2
    if k == b:
        print("Bon Appetit")
    else:
        print(b-k)

if __name__ == '__main__':
    nk = input().rstrip().split()

    n = int(nk[0])

    k = int(nk[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)
