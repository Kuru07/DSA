# Problem Statement: You are given an array of integers, your task is to move all the zeros in the array to the end of the array and move non-negative integers to the front by maintaining their order.
# Complexity : O(n) where n is the number of elements in the array. 

class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        for num in nums:
            if num!=0:
                nums[i]=num
                i+=1
        while i<n:
            nums[i]=0
            i+=1
        
sol=Solution()
nums=[0,1,0,3,12]
sol.moveZeroes(nums)
print(nums)
