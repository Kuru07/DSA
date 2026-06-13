# Problem Statement: There’s an array ‘A’ of size ‘N’ with an equal number of positive and negative elements.
#  Without altering the relative order of positive and negative elements, you must return an array of alternately positive and negative values.

# Complexity Analysis: O(n) where n is the number of elements in the input array.

nums =[3,1,-2,-5,2,-4]
ans=[0]*len(nums)
p,n=0,1
for i in range(len(nums)):
    if nums[i]>0:
        ans[p]=nums[i]
        p+=2
    else:
        ans[n]=nums[i]
        n+=2
        
print(ans)

