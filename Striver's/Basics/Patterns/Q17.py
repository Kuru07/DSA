"""
Pattern 17
      A      
     ABA     
    ABCBA    
   ABCDCBA   
  ABCDEDCBA  
  
"""

n=5
for i in range(n):
    num=ord('A')
    left=n-i+1
    l=[chr(num+j) for j in range(i+1)]
    seq=l+l[:-1][::-1]
    print(" "*(left),end="")
    print(''.join(seq),end="")
    print(" "*(left))