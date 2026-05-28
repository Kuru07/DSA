# Problem Description: Given an integer N, write a program to print numbers from 1 to N.

# Complexity Analysis: Time complexity: O(N) Space complexity: O(N) (due to recursive stack space)
def printNum(count,n):
    if count==n:
        print(count)
        return
    print(count,end=", ")
    
    return printNum(count+1,n)
    
printNum(1,5)
