//To find intersection betwwn two unsorted arrays

class Solution {
    public static int numberofElementsInIntersection(int a[], int b[]) {
        int i=0,j=0;
        List<Integer> arr=new ArrayList<>();
        Arrays.sort(a);
        Arrays.sort(b);
        while(i<a.length && j<b.length)
        {
            if(a[i]==b[j])
            {
                arr.add(a[i]);
                i++;
                j++;
            }
            else if(a[i]<b[j])
            i++;
            else
            j++;
        }
        return arr.size();
    }
}