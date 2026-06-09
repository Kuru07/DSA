# Problem Statement: Given a sorted array of N integers and an integer x, write a program to find the upper bound of x.
# Complexity: O(N) time and O(1) space

nums = [3,5,8,9,15,19]
n=len(nums)
x=9
yes=True
for i in range(len(nums)):
    if nums[i]>x:
        print(i)
        yes=False
        break

if yes:
    print(n)