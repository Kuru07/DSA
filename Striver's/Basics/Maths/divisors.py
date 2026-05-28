#Print all Divisors of a given Number

# Complexity Time - O(n) , Space - O(n)

n=12
l=[x for x in range(1,n+1) if (n%x==0)]
print(l)