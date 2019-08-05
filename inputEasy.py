n,m = map(int, input().split())
arr = list(map(int, input().split()))
a = set(map(int, input().split()))
b = set(map(int,input().split()))

print(n,m)
print(arr)
print(a)
print(b)


c = 0
for i in arr:
    if i in a:
        c = c +1
    if i in b:
        c = c-1
print(c)
