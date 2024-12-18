//To search a 2d array which is sorted in each row. Time complexity is O(log(m*n))

class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int m=0,n=0;
        m=matrix.length;
        boolean flag=false;
        for(int i=0;i<m;i++)
        {
            n=matrix[i].length;
            if(target>matrix[i][n-1])
            continue;
            else
            {
                for(int j=0;j<n;j++)
                {
                    if(target==matrix[i][j])
                    flag=true;
                }
            }
        }
        return flag;
    }
}