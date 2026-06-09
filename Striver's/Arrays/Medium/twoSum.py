# Problem Statement: Given an array of integers arr[] and an integer target.

# Complexity : O(n) time and O(n) space

nums = [3,2,4]
target=6
start=0
end=start+1
exist=False
while start<end:
    if nums[start] + nums[end] == target:
        exist=True
        break
    if end==len(nums)-1:
        start+=1
        end=start+1
        continue
    end+=1

print(start,end)
print("Exist",exist)