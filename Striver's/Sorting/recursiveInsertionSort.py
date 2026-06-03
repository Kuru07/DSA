# Problem Statement: Given an array of N integers, write a program to implement the Recursive Insertion Sort algorithm.

# Complexity Analysis: Time complexity: O(N^2) Space complexity: O(N) due to recursive stack space.

def insertion_sort(arr, i, n):
    # Base case
    if i == n:
        return

    j = i
    # Move the element to the left while it's smaller than its predecessor
    while j > 0 and arr[j - 1] > arr[j]:
        # Swap
        arr[j - 1], arr[j] = arr[j], arr[j - 1]
        j -= 1

    # Recur for the next index
    insertion_sort(arr, i + 1, n)

# Driver code
arr = [13, 46, 24, 52, 20, 9]
n = len(arr)

print("Before Using Insertion Sort:")
print(arr)

insertion_sort(arr, 0, n)

print("After Using Insertion Sort:")
print(arr)
