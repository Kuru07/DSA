# Selection Sort
# Use min index and swap the current element with the min element

arr=[13,46,24,52,20,9]
n=len(arr)
for i in range(n):
    min_pos=i
    for j in range(i+1,n):
        if arr[j]<arr[min_pos]:
            min_pos=j
      
    temp=arr[i]
    arr[i]=arr[min_pos]
    arr[min_pos]=temp      

print(arr)