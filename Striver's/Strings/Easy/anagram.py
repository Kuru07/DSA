# Problem Statement: Given two strings, check if two strings are anagrams of each other or not.
# The count of every letter of both strings are equal.

# Complexity Analysis: Time complexity: O(N) Space complexity: O(N)

from collections import Counter

s="cat"
t="act"
def isAnagram( s, t):
    return Counter(s)==Counter(t)