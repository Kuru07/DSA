# Problem Statement: Given an array of size n, write a program to check if the given array is sorted in (ascending / Increasing / Non-decreasing) order or not. If the array is sorted then return True, Else return False.

def isSorted(arr, n):
    for i in range(1, n):
        if arr[i] < arr[i - 1]: 
            return False
    return True  

arr = [1, 2, 3, 4, 5]
n = len(arr)

print("True" if isSorted(arr, n) else "False")

#  Given an array nums, return true if the array was originally sorted in non-decreasing order, then rotated some number of positions (including zero). Otherwise, return false.
# For example, [0,1,2,4,5,6,7] might be rotated to become [4,5,6,7,0,1,2]. 


class Solution:
    def check(self, nums: List[int]) -> bool:
        n=sum(nums[i-1] > v for i,v in enumerate(nums))
        return True if n<=1 else False
