"""
Pattern 7
    *
   ***
  *****
"""


n=3
for i in range(n):
    print(" "*(n-i-1),end="")
    print(''.join(["*"]*(2*i+1)),end="")
    print(" "*(n-i-1))