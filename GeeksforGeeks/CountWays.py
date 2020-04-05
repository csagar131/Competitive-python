#Count ways to reach the n’th stair

# Recurssive program to find n'th fibonacci number 
def fib(n): 
	if n <= 1: 
		return n 
	return fib(n-1) + fib(n-2) 

# returns no. of ways to reach s'th stair 
def countWays(s): 
	return fib(s + 1) 

# Driver program 

s = 2
print "Number of ways = ", 
print countWays(s) 
