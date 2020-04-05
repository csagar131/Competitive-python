#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    lst2 = s.split(':')
    last = str(lst2[-1:][0][2:])
    lst1 = s.split(':')[-3:-1]
    for i in range(0,len(lst1)):
        lst1[i] = int(lst1[i])
    
    result = ''
    if lst1[0] == 12 and last == 'AM':
        result = result + '00:' + str(lst1[1]) + ':' + str(lst2[-1:][0][:2])
        print(result)
    elif lst1[0] == 12 and last == 'PM':
        result = result + '12:00:00'
    else:
        if last == 'AM':
            spt = s.split(':')
            hh = int(spt[0])
            ss = spt[-1][:2]
            result = result +'0'+ str(hh) +':'+ spt[1] +':' + ss
            
        else:
            spt = s.split(':')
            hh = int(spt[0])
            hh = hh + 12
            ss = spt[-1][:2]
            #print(ss)
            result = result + str(hh) +':'+ spt[1] +':' + ss
    return result
        

    
    #print(lst1)
    #print(last)
    


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
