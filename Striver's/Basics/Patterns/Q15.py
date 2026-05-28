"""
Pattern 15
A B C D E 
A B C D 
A B C 
A B 
A 
"""

n=5
for i in range(n,0,-1):
    num=ord('A')
    for j in range(i):
        print(chr(num),end=" ")
        num+=1
    print()