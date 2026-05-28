# Problem Description: Given an integer N, write a program to print numbers from N to 1.

# Complexity Analysis: Time complexity: O(N) Space complexity: O(N) (due to recursive stack space)

def printNum(n):
    if n==1:
        print(n)
        return
    print(n,end=", ")
    
    return printNum(n-1)
    
printNum(5)