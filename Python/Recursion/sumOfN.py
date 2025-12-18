def sumofN(n):
    if n==0:
        return 0
    return n+sumofN(n-1)

print(sumofN(7))