# Problem Statement: Given an input string, containing upper-case and lower-case letters, digits, and spaces( ' ' ). 
# A word is defined as a sequence of non-space characters. The words in s are separated by at least one space. 
# Return a string with the words in reverse order, concatenated by a single space.

# Complexity Analysis: Time complexity: O(N) Space complexity: O(N)

s = " amazing coding skills "
out=" ".join(s.strip().split()[::-1])
print(out)