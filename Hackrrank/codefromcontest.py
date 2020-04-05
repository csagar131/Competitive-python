def findgcd(k,l):
    if l == 0:
        return k
    else:
        return findgcd(l,k%l)

t = int(input())
while t > 0:
    t= t-1
    n,m = input().split()
    n = int(n)
    m = int(m)
    lst = []
    c = 0
    for i in range(n+1,n+1000):
        s=findgcd(n,i)
        if s == 2:
            c = c+1
            lst.append(i)
        if c == 3:
            break
    for i in lst:
        print(i,end=" ")
            
