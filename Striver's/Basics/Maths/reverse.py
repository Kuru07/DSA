# Problem Statement: Given an integer N return the reverse of the given number.

# Complextity Time - O(logN) , Space - O(1)
num=10400
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10

print(rev)