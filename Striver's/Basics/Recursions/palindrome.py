# Problem Statement: Given a string, check if the string is palindrome or not. A string is said to be palindrome if the reverse of the string is the same as the string.
# Complexity Analysis: Time complexity: O(N) Space complexity: O(1)
st="ABCDCBA"
if st == st[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")
