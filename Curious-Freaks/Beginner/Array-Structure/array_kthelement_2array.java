//To find kth element in a 2 sorted array combined and sorted

class Solution {
    public int kthElement(int a[], int b[], int k) {
        int temp[]=new int[a.length+b.length];
        for(int i=0;i<temp.length;i++)
        {
            if(i<a.length)
            temp[i]=a[i];
            else
            temp[i]=b[i-a.length];
        }
        Arrays.sort(temp);
        return temp[k-1];
    }
}