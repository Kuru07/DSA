//To find palindrome of a number
class Solution
{
    public String is_palindrome(int n)
    {
        int rev=0,temp=n;
        while(temp>0)
        {
            rev=rev*10+temp%10;
            temp/=10;
        }
        if(n==rev)
        return "Yes";
        else
        return "No";
    }
}