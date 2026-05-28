"""
Pattern 14
A 
A B 
A B C 
A B C D 
A B C D E 

"""
n=5
for i in range(n):
    num=ord('A')
    for j in range(i+1):
        print(chr(num),end=" ")
        num+=1
    print()