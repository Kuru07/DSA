from math import *

num=789
temp=num
rev=0
count=0

# Using Log Method

def countDigits(n):
    return int(log10(n)+1)

# Normal method , Palindrome and Reverse
while temp>0:
    digit=temp%10
    print(digit)
    rev=rev*10+digit
    temp=temp//10
    count+=1
print("Total Digits:",count)
print("Reversed Number:",rev)

print("Count using log method: ",countDigits(num))


# Armstrong number

def armstrong(n):
    temp=n
    nod=len(str(n))
    sum=0
    while temp >0 :
        digit=temp%10
        sum+=digit**nod
        temp=temp//10

    if sum == n:
        print(n,"is an Armstrong number")
    else:
        print(n,"is not an Armstrong number")

armstrong(153)