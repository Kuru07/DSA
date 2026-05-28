# Problem Statement: Given an integer N. Print the Fibonacci series up to the Nth term.

# Complexity Analysis: Time complexity: O(N) Space complexity: O(1)

a=0
b=1
n=int(input("Enter Number: "))
print(a,end=" ")
print(b,end=" ")
for _ in range(n-1):
    s=a+b
    print(s,end=" ")
    a=b
    b=s