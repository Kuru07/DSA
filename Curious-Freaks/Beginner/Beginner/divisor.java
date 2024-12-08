//Divisor
public class Solution{
    public static List< Integer > printDivisors(int n) {
      List<Integer> al=new ArrayList<Integer>();
      int d=n;
      while(d>0)
      {
          if(d!=0 && n%d==0)
          al.add(d);
          d--;
      }
      Collections.reverse(al);
      return al;

    }
}