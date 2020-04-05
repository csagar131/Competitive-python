from collections import Counter
x = int(input())
ls = input().split()
for i in range(len(ls)):
    ls[i] = int(ls[i])
n = int(input())
ss =[]
for i in range(n):
    ss.append(input().split())
for i in range(n):
    for j in range(0,2):
        ss[i][j]= int(ss[i][j])

ls=dict(Counter(ls))

s = 0
for i in range(0,len(ss)):
    k = ss[i][0]
    try:
        if ls.get(k) is not 0 and ls.get(k) is not None:
            s = s+ss[i][1]
            ls[k] = ls.get(k)-1
    except:
        pass
print(s)

