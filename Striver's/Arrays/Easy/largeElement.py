# Problem Statement: Given an array, we have to find the largest element in the array.

# Complexity Analysis: Time complexity: O(N) Space complexity: O(1)
arr=[13,46,24,52,20,9]
n=len(arr)
maxEle=arr[0]
for i in range(1,n):
    if arr[i]>maxEle:
        maxEle=arr[i]
        
print(maxEle)