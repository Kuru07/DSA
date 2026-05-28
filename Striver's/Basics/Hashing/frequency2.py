# Problem Statement: Problem Statement: Given an array of size N. Find the highest and lowest frequency element.
# Complexity Analysis: Time complexity: O(N) Space complexity: O(N)
from collections import Counter

arr=[10,5,10,15,10,5]
freq=Counter(arr)
min_freq=min(freq.items(),key=lambda x: x[1])
max_freq=max(freq.items(),key=lambda x: x[1])
print(max_freq[0],end=" ")
print(min_freq[0])