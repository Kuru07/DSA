//To find armstrong number
class Solution {
    static boolean armstrongNumber(int n) {
        int sum=0,temp=n,digit=(Integer.toString(n)).length();
        while(temp>0)
        {
            sum+=(int)(Math.pow(temp%10,digit));
            temp/=10;
        }
        if(n==sum)
        return true;
        else
        return false;
        
    }
}