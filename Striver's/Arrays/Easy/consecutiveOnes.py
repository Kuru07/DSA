# Given a binary array nums, return the maximum number of consecutive 1's in the array.
# Complexity : O(n) where n is the number of elements in the array.

nums=[1, 0, 1, 1, 0, 1]
ones=[]
count=0
skip=False
for num in nums:
    if num==1:
        count+=1
        skip=False
    if num==0 and not skip:
        ones.append(count)
        skip=True
        count=0
ones.append(count)
print(max(ones))
