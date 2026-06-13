# Problem Statement: You are given an array of prices where prices[i] is the price of a given stock on an ith day. 
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock. Return the maximum profit you can achieve from this transaction.
#  If you cannot achieve any profit, return 0.

nums=[7,1,5,3,6,4]
n=len(nums)
maxPrice=0
j=0
i=j+1

while i < n and j<n:
    print(nums[i],nums[j],nums[i] - nums[j],maxPrice)
    if nums[i] - nums[j] > maxPrice:
        maxPrice=nums[i] - nums[j]
    i+=1
    if i==n:
        j+=1
        i=j+1
        
print(maxPrice)

#Optimal Solution

def maxProfit(prices) :
    minPrice=float('inf')
    maxProfit=0
    for price in prices:
        if minPrice > price:
            minPrice=price
        else:
            maxProfit = max(maxProfit,price-minPrice)
    return maxProfit
