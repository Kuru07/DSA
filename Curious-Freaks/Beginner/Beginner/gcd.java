//GCD of 2 number

class Solution {
    public static int gcd(int a, int b) {
       if(a==0)
       return b;
       else if(b==0)
       return a;
       else if(b<a)
       return gcd(b,a%b);
       else
       return gcd(a,b%a);
    }
}
     