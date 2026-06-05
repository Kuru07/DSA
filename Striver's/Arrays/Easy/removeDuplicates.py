'''
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.

'''

# Complexity Analysis
# Time Complexity: O(n), where n is the number of elements in the input array. We traverse the array once to remove duplicates.

arr=[1,1,1,2,2,3,3,3,3,4,4]

def distinctElement(arr):
    
    if not arr:
        return 0
    
    index=0
    for i in range(1,len(arr)):
        
        if arr[index] != arr[i]:
            index+=1
            arr[index]=arr[i]
            
    return index+1
    
    
print(distinctElement(arr))
        
        
