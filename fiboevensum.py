t = int(input())
while t is not 0:
    t = t -1
    n = int(input())
    p = 1
    q = 1
    lst = []
    if n == 1:
        print("1")
        break
    for i in range(n-1):
        if i == 0:
            lst.append(p)
            lst.append(q)
        else:
            r = p + q
            p = q
            q = r
            lst.append(r)
    print(lst)
    s = sum([i for i in lst if i%2==0])
    print(s)
