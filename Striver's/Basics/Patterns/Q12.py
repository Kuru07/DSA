"""
Pattern 12
1      1
12    21
123  321
12344321

"""

n=4
for i in range(n):
    l=[int(x+1) for x in range(i+1)]
    s=''.join(map(str,l))
    print(s,end="")
    print(" "*(2*(n-i-1)),end="")
    print(s[::-1])
    