//To find the frequency of occurenece of an element in an array
class Solution {
    public List<Integer> frequencyCount(int[] arr) {
        
        int[] count=new int[arr.length];
        
        for(int i=0;i<arr.length;i++)
        count[i]=0;
        
        for(int i:arr)
        count[i-1]++;
        
        List<Integer> temp=new ArrayList<>();
        for(int i:count)
        temp.add(i);
        
        return temp;
    }
}