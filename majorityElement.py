

from collections import Counter
t = int(input())
while t is not 0:
    t = t-1
    n = int(input())
    lst = [int(num) for num in input().split()]
    c = Counter(lst)
    #print(c)
    res = dict((v,k) for k,v in c.items())
    #print(res)
    #print(res[max(list(c.values()))])
    if max(list(c.values())) > n // 2:
        print(res[max(list(c.values()))])
    else:
        print("-1")
