# Factors of a number

#Brute Force Method
def factors_bruteForce(n):
    result =[]
    for i in range(1,n+1):
        if n%i==0:
            result.append(i)
    return result

fact=factors_bruteForce(28)
print("Factors of 28 are:",fact)

#Normal Method
def factors_better(n):
    result =[]
    for i in range(1,n//2 + 1):
        if n%i==0:
            result.append(i)
    result.append(n)
    return result

fact=factors_better(28)
print("Factors of 28 are:",fact)

# Optimal Method
from math import sqrt

def factors_optimal(n):     
    result=[]
    for i in range(1,int(sqrt(n))+1):
        if n%i==0:
            result.append(i)
            if n//i != i:
                result.append(n//i)
    result.sort()
    return result

fact=factors_optimal(28)
print("Factors of 28 are:",fact)