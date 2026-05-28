"""
Pattern 18
E 
D E 
C D E 
B C D E 
A B C D E 

"""

n=5
for i in range(n):
    num=ord('A')+n-1-i
    for j in range(i+1):
        print(chr(num),end=" ")
        num+=1
    print()