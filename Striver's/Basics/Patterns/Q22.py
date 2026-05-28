"""
Pattern 22
4444444
4333334
4322234
4321234
4322234
4333334
4444444

"""

n=4
for i in range(2*n-1):
    for j in range(2*n-1):
        top=i
        bottom=j
        left=(2*n-2)-i
        right=(2*n-2)-j
        pos=min(top,bottom,left,right)
        print(n-pos,end="")
    print()