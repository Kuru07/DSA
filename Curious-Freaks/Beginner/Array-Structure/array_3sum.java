//To find triplet sum - triplet with sum in array possible or not

class Solution {
    public static boolean hasTripletSum(int arr[], int target) {
      for(int i=0;i<arr.length-2;i++){
            for(int j=i+1;j<arr.length-1;j++)
            {
                for(int k=j+1;k<arr.length;k++)
                {
                    if((arr[i]+arr[j]+arr[k]==target))
                    return true;
                }
            }
        }
        return false;
    }
}
