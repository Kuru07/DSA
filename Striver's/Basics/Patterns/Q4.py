"""
pattern 4
1
22
333
4444

"""
n=5
num=1
for i in range(n):
    l=[num]*(i+1)
    print(' '.join(map(str,l)))
    num+=1