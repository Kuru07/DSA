# Basic Dictionary method

def frequency(num):
    freq={}
    for i in range(0,len(num)):
        if num[i] in freq:
            freq[num[i]]+=1
        else:
            freq[num[i]]=1
    return freq

num=[1,5,7,23,4,5,1,2,22,11,7,23,2,6,8,9,45]
print("Frequency of elements in the list:")
print(frequency(num))

# Hash map
def hashMapFactors(num):
    hash_map={}
    n=len(num)
    for i in range(0,n):
        hash_map[num[i]]=hash_map.get(num[i],0)+1
    return hash_map

num=[10,20,10,30,40,20,10,50,60,30]
print("Hash map of factors:")
print(hashMapFactors(num))

# Two arrays and getting the frequency of one in another

n=[1,2,3,4,5,1,2,1,3,4,5,6,7,8,9]
m=[1,2,3,1,4,1,5,6,7]
mlen=len(m)
freq_map={}
for i in range(0,mlen):
    if ( m[i] in n ) & ( m[i] not in freq_map.keys() ):
        freq_map[m[i]]=n.count(m[i])
print("Frequency of elements of m in n:")
print(freq_map)
