"""
Pattern 16
A 
B B 
C C C 
D D D D 
E E E E E 
"""

n=5
num=ord('A')
for i in range(n):
    for j in range(i+1):
        print(chr(num),end=" ")
    num+=1
    print()