#   Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
#  If target exists, then return its index. Otherwise, return -1.

# Complexity Analysis: Time complexity: O(logN) Space complexity: O(1)
def search( nums, target) -> int:
    start=0
    end=len(nums)-1
    while start<=end:
        mid=(start+end)//2
        if nums[mid]==target:
            return mid
        if nums[mid]<target:
            start=mid+1
        if nums[mid]>target:
            end=mid-1
    return -1