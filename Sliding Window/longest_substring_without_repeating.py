
Real-world intuition:
This problem models situations where we want the longest sequence
without repetition, such as:
- Longest unique password characters
- Network packets without duplicate IDs
- Text processing and data validation

Approach:
We use the Sliding Window technique.
A window is expanded using a right pointer.
If a duplicate is found, we shrink the window from the left
until all characters are unique again.

Why Sliding Window?
Because checking all substrings would be too slow (O(n²)).
Sliding window gives an optimal O(n) solution.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_set = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in char_set:
                char_set.remove(s[left])
                left += 1

            char_set.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
