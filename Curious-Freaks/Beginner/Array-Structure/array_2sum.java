//To find two sum - pair with sum in array possible or not
class Solution {
    boolean twoSum(int arr[], int target) {
        for(int i=0;i<arr.length-1;i++){
            for(int j=i+1;j<arr.length;j++)
            {
                if((arr[i]+arr[j]==target))
                return true;
            }
        }
        return false;
    }
}