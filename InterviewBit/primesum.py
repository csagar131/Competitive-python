'''
Given an even number ( greater than 2 ), return two prime numbers whose sum will be equal to given number.
'''


import math
class Solution:
    # @param A : integer
    # @return a list of integers
    def primesum(self, A):
        lst = []
        number = [1]*(A+1)
        number[0] = 0
        number[1] = 0
        for i in range(2,int(math.sqrt(A))+1):
            if number[i] == 1:
                j = 2
                while i*j <=A:
                    number[i*j] = 0
                    j+=1
        
        for i in range(0,len(number)):
            if number[i] == 1 and number[A-i] == 1:
                lst.append(i)
                lst.append(A-i)
                return lst
                        
                        
                        
            
