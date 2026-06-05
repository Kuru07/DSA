# Problem Statement: Given an array, and an element num the task is to find if num is present in the given array or not. If present print the index of the element or print -1.
# Complexity : O(n) where n is the number of elements in the array.
nums=[1,2,3,4,5]
k=7
if k in nums:
    print(nums.index(k))
else:
    print(-1)