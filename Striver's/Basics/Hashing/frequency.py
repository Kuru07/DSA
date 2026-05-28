# Problem Statement: Given an array, we have found the number of occurrences of each element in the array.

# Complexity Analysis: Time complexity: O(N) Space complexity: O(N)
from collections import Counter

arr=[2,2,3,4,4,2]
freq=Counter(arr)
for k,v in freq.items():
    print(k,end=": ")
    print(v)