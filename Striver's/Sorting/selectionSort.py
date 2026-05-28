# Problem Statement: Given an array of N integers, write a program to implement the Selection sorting algorithm.
# Complexity Analysis: Time complexity: O(N^2) Space complexity: O(1)
arr=[13,46,24,52,20,9]
n=len(arr)
for i in range(n):
    min_pos=i
    for j in range(i+1,n):
        if arr[j]<arr[min_pos]:
            min_pos=j
      
    temp=arr[i]
    arr[i]=arr[min_pos]
    arr[min_pos]=temp      

print(arr)

