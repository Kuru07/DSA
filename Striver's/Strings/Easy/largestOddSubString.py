# You are given a string num, representing a large integer. 
# Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.

# Complexity Analysis: Time complexity: O(N) Space complexity: O(1)

num="52"

for i in range(len(num)-1,-1,-1):
    if int(num[i])%2!=0:
        print( num[:i+1])
        break

print("")