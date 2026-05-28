"""
Pattern 5
*****
****
***
**  
"""

n=5
s=n
for i in range(n):
    p=["*"] * s
    print(' '.join(p))
    s-=1