//To find the no of digits that evenly divide a number

class Solution {
    static int evenlyDivides(int n) {
        int temp=n,count=0;
        while(temp>0)
        {
            int d=temp%10;
            if(d!=0 && n%d==0)
            count++;
            temp/=10;
        }
        return count;
    }
}