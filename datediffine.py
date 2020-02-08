# Enter your code here. Read input from STDIN. Print output to STDOUT
from datetime import date,datetime,timedelta

d1 = map(int,input().split(' '))
d2 = map(int,input().split(' '))
l1 = list(d1)
l2 = list(d2)
a =  date(l1[2],l1[1],l1[0])
e =  date(l2[2],l2[1],l2[0])


def getfine():
    result = 0
    if (e-a).days >=0:
        result = 0
        #return result
        if (e-a).days <=0:
            result = 15 * abs((a-e).days)
            return result
        return result 
     
    elif a.year - e.year >=1 :
        result = 10000
        return result
    elif a.month - e.month >=1:
        result = 500 * (a.month - e.month)
        return result

    elif (a-e).days > 0 :
        result = 15 * (a-e).days
        return result

    
    
print(getfine())



