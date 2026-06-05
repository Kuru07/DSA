# Problem Statement: Given an array nums of size n and an integer k, find the length of the longest sub-array that sums to k. If no such sub-array exists, return 0.



nums = [10, 5, 2, 7, 1, 9]
k = 15 
sub=0

for i in range(len(nums)):
    j=i
    tot=0
    while j < len(nums):
        tot+=nums[j]
        j+=1
        if tot-k ==0 and sub < j-i:
            sub=j-i
print(sub)