//Revrese an array

class Solution {
    public void reverseArray(int arr[]) {
        int n=arr.length;
        int k=0;
       int[] temp=new int[n];
       for(int i=0;i<n;i++)
       {
           temp[i]=arr[i];
           k=i;
       }
       for(int i=0;i<n;i++)
       {
           arr[i]=temp[k];
           k--;
       }
    }
}

//Method -2 
class GfG {
    
    // function to reverse an array
    static void reverseArray(List<Integer> arr) {
        Collections.reverse(arr);
    }

    public static void main(String[] args) {
        List<Integer> arr = 
          new ArrayList<>(Arrays.asList(1, 4, 3, 2, 6, 5));

        reverseArray(arr);
  
        for (int i = 0; i < arr.size(); i++) 
            System.out.print(arr.get(i) + " ");
    }
}