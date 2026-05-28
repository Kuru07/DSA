"""
Pattern 11
1
01
101
0101
10101


"""

n=5
for i in range(n):
    for j in range(i+1):
        if (i%2==0):
            if (j%2==0):
                print("1",end="")
            else:
                print("0",end="")
        else:
            if (j%2==0):
                print("0",end="")
            else:
                print("1",end="")
    print()