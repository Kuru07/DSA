//TO rotate an array by an integer k
public class Solution {
	public static ArrayList<Integer> rotateArray(ArrayList<Integer> arr, int k) {
        for(int j=0;j<k;j++)
	    {
		Integer temp=arr.get(0);
        for(int i=0;i<arr.size()-1;i++)
        {
            arr.set(i,arr.get(i+1));
        }
        arr.set(arr.size()-1,temp);
	    }
        return arr;
    }
}