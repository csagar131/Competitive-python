# Enter your code here. Read input from STDIN. Print output to STDO                                                         
n = int(input())
max_num = 0
max_stack = [0]
stack = []
for _ in range(n):
    lst = list(map(int,input().split(" ")))
    if lst[0] == 1:
        stack.append(lst[1])
        if lst[1] > max_num:
            max_num = lst[1]
            max_stack.append(max_num)
    if lst[0] == 2:
        if stack:
            value=stack.pop()
        if max_stack[len(max_stack)-1] == value:
            max_stack.pop()
            max_num = max_stack[len(max_stack)-1]
                        
    if lst[0] == 3:
        print(max_stack[len(max_stack)-1])










