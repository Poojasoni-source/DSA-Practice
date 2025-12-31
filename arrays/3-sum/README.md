# Three Sum Finder

## Description
This program finds all **unique triplets** in an integer array that sum up to a target value `K` (default 0).  
It demonstrates array manipulation, sorting, and the two-pointer technique.

## Problem Statement
- **Input:** Array of integers `arr` and target sum `K`.  
- **Output:** List of unique triplets `[a, b, c]` such that `a + b + c = K`.  
- **Constraints:** Triplets must be unique and elements must come from different indices.
## Approach
1. Sort the array.  
2. Fix one element and use **two-pointer technique** for the remaining array.  
3. Skip duplicates to ensure unique triplets.  
4. Return the list of triplets.

## Real-World Applications
- **Finance:** Detect three transactions that sum to a suspicious amount.  
- **E-commerce:** Find three items matching a gift card value.  
- **Gaming:** Combine three power-ups or scores to reach a target.
- ## Time & Space Complexity
- **Time Complexity:** O(n²)  
- **Space Complexity:** O(1) ignoring output
