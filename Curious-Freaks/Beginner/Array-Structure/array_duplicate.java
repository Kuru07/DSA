//To remove duplicates from an sorted array and return the count

class Solution {
    // Function to remove duplicates from the given array
    public int removeDuplicates(int[] arr) {
        int count=0;
        for(int i=1;i<arr.length;i++)
        {
            if(arr[i]!=arr[count])
            {
                count++;
                arr[count]=arr[i];
            }
        }
        return count+1;
    }
}
