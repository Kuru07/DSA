////To find triplet sum - triplet with sum equals 0 in array possible or not


class Solution {
    // Function to find triplets with zero sum.
    public boolean findTriplets(int[] arr) {
       for(int i=0;i<arr.length-2;i++){
            for(int j=i+1;j<arr.length-1;j++)
            {
                for(int k=j+1;k<arr.length;k++)
                {
                    if((arr[i]+arr[j]+arr[k]==0))
                    return true;
                }
            }
        }
        return false;
    }
}