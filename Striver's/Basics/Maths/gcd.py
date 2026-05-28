# Problem Statement: Given two integers N1 and N2, find their greatest common divisor.

# Complextity Time - O(log(min(N1,N2))) , Space - O(1)
a=int(input("Enter N1: "))
b=int(input("Enter N2: "))

while b:
    a,b=b,a%b

print(a)