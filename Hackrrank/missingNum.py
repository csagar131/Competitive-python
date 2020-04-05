t = int(input())
while t is not 0:
    t = t - 1
    n = int(input())
    lst = set([int(num) for num in input().split()])
    lst2 = set(list(range(1,n+1)))
    #print(lst)
    k=str(lst2.difference(lst)).replace('{','').replace('}','')
    print(k)
    
    #for i in lst2:
        #if i not in lst:
            #print(i)
            #break
    
        
# for non optimized solution create a list with full number and
#        match with our main list    */
