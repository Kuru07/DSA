# Reverse an array in an range

nums=[1,5,7,2,3,4,6,8]

def reverseArray(start,end,nums):
    if start>=end:
        return
    nums[start],nums[end]=nums[end],nums[start]
    reverseArray(start+1,end-1,nums)
    return nums

print(reverseArray(2,6,nums))
