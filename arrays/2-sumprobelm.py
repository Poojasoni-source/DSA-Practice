"""
Two Sum Finder
Author: Your Name
Description: Given an integer array 'arr' and a target 'K', this program finds
the indices of two numbers in the array that add up to K.
"""

def two_sum(arr, K):
    """
    Find indices of two numbers in 'arr' that sum to 'K'.

    Parameters:
    arr (list): List of integers
    K (int): Target sum

    Returns:
    list: Indices of the two numbers, or None if no pair exists
    """
    num_to_index = {}  # stores number -> index
    for i, num in enumerate(arr):
        complement = K - num
        if complement in num_to_index:
            return [num_to_index[complement], i]  # found the pair
        num_to_index[num] = i
    return None

# Example usage
if __name__ == "__main__":
    arr = [3, 8, 12, 17]
    K = 20
    result = two_sum(arr, K)
    print("Array:", arr)
    print("Target Sum:", K)
    print("Indices of numbers that sum to K:", result)
