# Problem Statement: Given a number X,  print its factorial.
# Complexity Analysis: Time complexity: O(N) Space complexity: O(N) (due to recursive stack space)

def factorial(n):
    if n==1:
        return 1

    return n * factorial(n-1)
    
print(factorial(5))