# Palindrome

def palindrome(s,left,right):
    if left>=right:
        return True
    if s[left]!=s[right]:
        return False
    return palindrome(s,left+1,right-1)
    

s="ABCDEFDCBA"

print(s + " is a a palindrome: "+str(palindrome(s,0,len(s)-1)))
