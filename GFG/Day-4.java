//Rotate an array by d digit to left
class Solution {
    // Function to rotate an array by d elements in counter-clockwise direction.
    static void rotateArr(int arr[], int d) {
        int n = arr.length;

        // Handle case when d > n
        d %= n;
        
        // Storing rotated version of array
        int[] temp = new int[n];

        // Copy last n - d elements to the front of temp
        for (int i = 0; i < n - d; i++)
            temp[i] = arr[d + i];

        // Copy the first d elements to the back of temp
        for (int i = 0; i < d; i++)
            temp[n - d + i] = arr[i];

        // Copying the elements of temp in arr
        // to get the final rotated array
        for (int i = 0; i < n; i++)
            arr[i] = temp[i];
    }
}