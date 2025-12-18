# Print 1 to N

def printNumbers(n):
    if n<=0:
        return
    printNumbers(n-1)
    print(n)

printNumbers(5)