//Number power of the reverse number
class Solution {
    public int reverseExponentiation(int n) {
       int rev=0,temp=n;
	    while(temp>0)
	    {
	        int d=temp%10;
	        rev=rev*10+d;
	        temp=temp/10;
	    }
	    return (int)Math.pow(n,rev);
    }
}
