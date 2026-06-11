# Problem Statement: Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
# A shift on s consists of moving the leftmost character of s to the rightmost position. For example, if s = "abcde", then it will be "bcdea" after one shift.

# Complexity Analysis: Time complexity: O(N^2) Space complexity: O(N)

s = "rotation" 
goal = "tionrota"
def rotateString( s, goal):
    for i in range(0,len(s)):
        s=s[1:]+s[0]
        if s==goal:
            return True
    return False