# Problem Statement: Given an array of N integers, write a program to implement the Bubble Sorting algorithm.

# Complexity Analysis: Time complexity: O(N^2) Space complexity: O(1)

arr=[13,46,24,52,20,9]
n=len(arr)
for i in range(n):
    swapped=False
    for j in range(0,n-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            swapped=True
    if not swapped:
        break
            
print(arr)