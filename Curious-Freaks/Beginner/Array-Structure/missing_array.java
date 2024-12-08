//To find the missing element in arr os size n-1, distinct integers from 1 to n(inclusive).
class Solution {
    int missingNumber(int arr[]) {
        Arrays.sort(arr);
        int n=arr.length;
        for(int i=1;i<=n;i++)
        {
            if(arr[i-1]!=i)
            return i;
        }
        return ++n;
    }
}