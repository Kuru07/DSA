//To push zeroes to the end in an array 
 
/*Method-1 -java


class Solution {
    void pushZerosToEnd(int[] arr) {
        int temp=-1,j=0;
       for(int i=0;i<arr.length;i++)
       {
           if(arr[i]!=0)
           {
                   temp=arr[j];
                   arr[j]=arr[i];
                   arr[i]=temp;
                   j++;
           }
       }
    }
}*/

//Method -2
#include <iostream>
using namespace std;

int main()
{
	int n = 5, j =4, temp;
	int arr[5] = {3,5,0,0,4};

	cout<<"Before Sort!"<<endl;
	for(int i = 0; i<n; i++)
	{
		cout<<arr[i]<<"\t";
	}

	for(int i= 0; i<n; i++)
	{
		if(arr[i-1] != 0)
		{
			if(arr[i] == 0)
			{
				for(int k = i; k<n-1; k++)
				{
					arr[k] = arr[k+1];
				}
				arr[j] = 0;
			}
		}
		else
		{
			for(int k = i-1; k<n-1; k++)
			{
				arr[k] = arr[k+1];
			}
			arr[j] = 0;
		}
	}
	j--;

	cout<<endl<<"After Sort!"<<endl;
	for(int i = 0; i<n; i++)
	{
		cout<<arr[i]<<"\t";
	}
}