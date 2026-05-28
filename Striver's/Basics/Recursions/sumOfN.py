# Problem Statement: Given a number ‘N’, find out the sum of the first N natural numbers .

# Complexity Analysis: Time complexity: O(N) Space complexity: O(N) (due to recursive stack space)
def sumofN(n):
    if n==0:
        return 0

    return n + sumofN(n-1)
    
print(sumofN(6))
