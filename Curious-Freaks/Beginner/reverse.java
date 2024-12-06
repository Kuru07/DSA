//Reverse a number
class Solution {
    public int reverseDigits(int n) {
        int temp=0;
	    while(n>0)
	    {
	        int d=n%10;
	        temp=temp*10+d;
	        n=n/10;
	        
	    }
	    return temp;
    }
}