##Two Sum Finder
##Description
This program finds two numbers in an array that sum to a given target value.
It is a common problem in arrays and is often used in coding interviews and real-world applications.

##Problem Statement
Input: Array of integers arr and target sum K.
Output: Indices of two numbers whose sum equals K.
Constraints: Each input has exactly one solution, and the same element cannot be used twice.
##Approach
Brute-force method: Check every pair of elements → O(n²)
Optimized method: Use a hashmap (dictionary) → O(n)
Traverse the array.
For each number num, check if K - num exists in the hashmap.
If yes, return the indices.
Else, store num in hashmap.
##Real-World Applications
E-commerce: Match two items to a gift card value.
Finance: Detect two transactions that sum to a specific amount.
Gaming: Combine two scores/power-ups to reach a target value.
##Time & Space Complexity
Time Complexity: O(n)
Space Complexity: O(n)
