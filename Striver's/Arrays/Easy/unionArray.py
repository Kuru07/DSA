# Problem Statement: Given two sorted arrays, arr1, and arr2 of size n and m. Find the union of two sorted arrays.

arr1=[1,2,3,4,5,6,7,8,9,10]
arr2=[2,3,4,4,5,11,12]
arr=list(set(arr1) | set(arr2))
print(sorted(arr))