# Problem Statement: Given an array of integers called nums, sort the array in non-decreasing order using the insertion sort algorithm and return the sorted array.
# Complexity Analysis: Time complexity: O(N^2) Space complexity: O(1)
arr=[13,46,24,52,20,9]
n=len(arr)
for i in range(1,n):
    key=arr[i]
    j=i-1
    while j>=0 and key <  arr[j]:
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
            
print(arr)