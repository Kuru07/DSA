# Problem Statement: Given an array, find the second smallest and second largest element in the array. Print ‘-1’ in the event that either of them doesn’t exist.
# Complexity Analysis: Time complexity: O(N) Space complexity: O(1)
arr=[1]
def largeSmall(arr):
    if len(arr)<=1:
        return (-1,-1)
    
    small,large=arr[0],arr[0]
    
    for i in range(len(arr)):
        if small > arr[i]:
            small=arr[i]
        if large < arr[i]:
            large=arr[i]
    
    smallest=float('inf')
    largest=float('-inf')
    for i in range(len(arr)):
        if arr[i] < smallest and arr[i] != small:
            smallest=arr[i]
        
        if arr[i] > largest and arr[i]!=large:
            largest=arr[i]
    return (smallest,largest)
    
(small,large)=largeSmall(arr)
        
print(f"Small : {small}")
print(f"Large: {large}")