//Given an integer array arr[]. You need to find the maximum sum of a subarray.

/* Kadane Algorithm

The idea of Kadane’s algorithm is to traverse over the array from left to right and for each element, 
find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values. 


But, the main issue is how to calculate maximum sum among all the subarrays ending at an element in O(1) time?


To calculate the maximum sum of subarray ending at current element, say maxEnding, 
we can use the maximum sum ending at the previous element. So for any element, we have two choices:


Choice 1: Extend the maximum sum subarray ending at the previous element by adding the current element to it. 
If the maximum subarray sum ending at the previous index is positive, then it is always better to extend the subarray.
Choice 2: Start a new subarray starting from the current element. If the maximum subarray sum ending at the previous index is negative, 
it is always better to start a new subarray from the current element.
This means that maxEnding at index i = max(maxEnding at index (i – 1) + arr[i], arr[i]) 
and the maximum value of maxEnding at any index will be our answer. */

class Solution {

    // arr: input array
    // Function to find the sum of contiguous subarray with maximum sum.
    int maxSubarraySum(int[] arr) {
        int max=arr[0];
        int res=arr[0];
        for(int i=1;i<arr.length;i++)
        {
            max=Math.max(max+arr[i],arr[i]);
            res=Math.max(max,res);
        }
        return res;
    }
}