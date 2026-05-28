"""
Pattern 20
*        *
**      **
***    ***
****  ****
**********
****  ****
***    ***
**      **
*        *

"""

n=5
for i in range(n):
    l="*" * (i+1)
    sp=" " * (2*(n-i-1))
    com=l+sp+l
    print(com)
for i in range(n-1,0,-1):
    l="*" * (i)
    sp=" " * (2*(n-i))
    com=l+sp+l
    print(com)