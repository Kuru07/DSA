# Problem Statement: Given an integer N, return the number of digits in N.


#Brute Force Approach Complexity Time - O(logN) , Space - O(1)
num=int(input("Enter number: "))
digit=0
while num>0:
    num=num//10
    digit+=1
print(digit)
    
#Optimal Approach Complexity Time - O(1) , Space - O(1)
import math
num=int(input("Enter number: "))
print(int(math.log10(num)+1))
    