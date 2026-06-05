# Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

# Complexity : O(n) where n is the number of elements in the array.

nums=[4,1,2,1,2]
ans=0
for num in nums:
    ans=ans^num
    
print(ans)
