"""
Pattern 6
12345
1234
123
12
1
"""
n=5
num=1
for i in range(n,0,-1):
    for j in range(i):
        print(num + j ,end="")
    print()