#Problem Statement:Given an integer N, return true it is an Armstrong number otherwise return false.

# Complexity Time - O(logN) , Space - O(1)

import math
num=8208
temp=num
digits=int(math.log10(num)+1)
su=0
while temp>0:
    digit=temp%10
    su=su+int(math.pow(digit,digits))
    temp=temp//10
print("Armstrong number" if num==su else "Not Armstrong")