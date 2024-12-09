//To find an array b is subset of an array a or not

class Solution {
    public boolean isSubset(int a[], int b[]) {
        HashSet<Integer> arr=new HashSet<>();
        for(int i:a)
        arr.add(i);
        for(int i:b)
        {
            if(!arr.contains(i))
            return false;
        }
        return true;
    }
}
