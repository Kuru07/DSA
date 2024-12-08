//To find a perfect number by adding its factors equal to original num
class Solution {
    static int isPerfectNumber(int n) {
        int fact=0,i=1;
        while(i<n)
        {
            if(n%i==0)
            fact=fact+i;
            i++;
        }
        if(n==fact)
        return 1;
        else
        return 0;
    }
};