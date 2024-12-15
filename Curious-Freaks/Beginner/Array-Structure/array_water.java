/*Given an array arr[] with non-negative integers representing the height of blocks. 
If the width of each block is 1, compute how much water can be trapped between the blocks during the rainy season. */

class Solution {
    public int trappingWater(int arr[]) {
        if(arr==null || arr.length<3)
        {
            return 0;
        }
       int left=0,right=arr.length-1,leftmax=0,rightmax=0,count=0;
       while(left<right)
       {
           if(arr[left]<arr[right])
           {
               if(arr[left]>=leftmax)
               {
                   leftmax=arr[left];
               }
               else
               {
                   count+=leftmax-arr[left];
               }
               left++;
           }
           else
           {
               if(arr[right]>=rightmax)
               {
                   rightmax=arr[right];
               }
               else
               {
                   count+=rightmax-arr[right];
               }
               right--;
           }
       }
       if(count<=0)
       return 0;
       else
       return count;
    }
}
