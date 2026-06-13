# Problem Statement: Given an integer array nums of size n, return the majority element of the array.
# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

# Complexity Analysis
# Time Complexity: O(n) where n is the number of elements in the input array.

from collections import Counter

nums = [3, 0, 0, 1, 3, 7, 2, 3, 7]
freq=Counter(nums)
print(max(freq.items(),key=lambda x:x[1])[0])