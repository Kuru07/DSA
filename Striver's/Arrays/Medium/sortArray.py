# Problem Statement: Given an array nums consisting of only 0, 1, or 2. Sort the array in non-decreasing order. The sorting must be done in-place, without making a copy of the original array.
 # Complexity Analysis: Time complexity: O(N) Space complexity: O(1)

nums = [1, 0, 2, 1, 0]
c0,c1,c2=0,0,0
for num in nums:
    if num==0:
        c0+=1
    if num==1:
        c1+=1
    if num==2:
        c2+=1

for i in range(c0):
    nums[i]=0

for i in range(c0,c1+c0):
    nums[i]=1

for i in range(c0+c1,c0+c1+c2):
    nums[i]=2
    
print(nums)