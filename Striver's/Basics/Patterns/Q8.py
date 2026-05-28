"""
Pattern 7
  *****
   ***
    *
  
"""

n=5
for i in range(n,0,-1):
    print(" "*(n-i),end="")
    print(''.join(["*"]*(2*i-1)),end="")
    print(" "*(n-i))