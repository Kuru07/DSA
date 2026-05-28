"""
Pattern 3
1
12
123

"""
n=5
num=1
for i in range(n):
    for j in range(i+1):
        l=[n]*(j+1)
        print(num + j ,end="")
    print()