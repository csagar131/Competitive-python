#https://practice.geeksforgeeks.org/problems/print-first-n-fibonacci-numbers/0

t = int(input())
while t is not 0:
    t = t -1
    n = int(input())
    p = 1
    q = 1
    if n == 1:
        print("1")
        break
    for i in range(n-1):
        if i == 0:
            print(str(p)+" "+str(q),end=' ')
        else:
            r = p + q
            p = q
            q = r
            print(r,end=' ')
    print()
            
            
