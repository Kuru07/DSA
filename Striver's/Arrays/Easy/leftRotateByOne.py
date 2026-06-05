# Problem Statement: Given an integer array nums, rotate the array to the left by one.

nums = [-1, 0, 3, 6]
temp=nums[0]
for i in range(1,len(nums)):
    nums[i-1]=nums[i]

nums[len(nums)-1]=temp

print(*nums)

# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

# Complexity Analysis:
# Time complexity: O(n*k) where n is the number of elements in the array and k is the number of rotations. This is because we are performing k rotations, and each rotation takes O(n) time to shift the elements.
# Space complexity: O(1) since we are modifying the array in-place and not using any additional data structures.

def rotate(nums, k):
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%len(nums)
        for _ in range(k):
            last=nums.pop()
            nums.insert(0,last)