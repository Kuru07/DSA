//To find Union of an array with duplicates

class Solution {
    public static int findUnion(int a[], int b[]) {
        int j=0,len1=0;
        int temp[]=new int[a.length+b.length];
        for(int i=0;i<a.length+b.length;i++)
        {
            if(i<a.length)
            temp[i]=a[i];
            else
            temp[i]=b[i-a.length];
        }
        Arrays.sort(temp);
        for(int i=0;i<temp.length-1;i++)
        {
            if(temp[i]!=temp[i+1])
            temp[j++]=temp[i];
        }
        temp[j++]=temp[temp.length-1];
        return j;

    }
}