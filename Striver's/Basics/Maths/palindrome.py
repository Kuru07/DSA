# Problem Statement: Given an integer N return true if the given number is palindrome else return false.

# Complextity Time - O(logN) , Space - O(1)
num=4554
tem=num
rev=0
while tem>0:
    rev=rev*10+tem%10
    tem=tem//10
print("Palindrome Number" if rev==num else "Not Palindrome")