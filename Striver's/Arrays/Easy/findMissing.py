# Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. 
# This array represents a permutation of the integers from 1 to n with one element missing. 
# Find the missing element in the array.

# Complexity : O(n) where n is the number of elements in the array.
arr=[8, 2, 4, 5, 3, 7, 1]
n=len(arr)
for i in range(1,n+1):
    if i not in arr:
        print(i)
        break