#Problem Description: Given an integer N, write a program to print your name N times.
# Complexity Analysis: Time complexity: O(N) Space complexity: O(N) (due to recursive stack space)

def printname(count,n):
    if count==n:
        return
    print("Kuru",end=" ")
    
    return printname(count+1,n)
    
printname(0,5)