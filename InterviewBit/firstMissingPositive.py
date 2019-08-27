mx = -1000
mn = 1000
for i in A:
    if i < mn and i > 0:
        mn = i
for i in A:
    if i > mx and i > 0:
        mx = i
    else:
        if mx > 1:
            break
        mx = 1

print("max is ",mx)
print("min ",mn)
        
        
for i in range(mn,mx+2):
    if i not in A:
        print(i)
        break

'''
        k = 0
        for i in A:
            if i == -(abs(i)):
                k = 1
            else:
                k = 0
                
        if k == 1:
            return k
        arr = [0]*(len(A)+1)
        for i in range(0,len(A)):
            if A[i] >=1 and A[i]<=len(arr):
                arr[A[i]]+=1
        for i in range(1,len(arr)):
            if arr[i] == 0:
                return i
                break
'''

'''
optimal suggested by interviewBIt
count = 0
        lst = []
        for i in range(0,len(A)):
            if A[i] > 0:
                count += 1
        if count == 0:
            return 1
        else:
            max1 = max(A)
            lst = [0] * (max1 + 2)
            for i in range(0,len(A)):
                if A[i] > 0:
                    lst[A[i]] = 1
            for i in range(1,len(lst)):
                if lst[i] == 0:
                    return i

'''
