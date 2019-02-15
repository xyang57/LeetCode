"""
5. Longest Palindromic Substring
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"
"""

"""
Solution:
    find the longest palindromic substring that starts with each index, and then compare them
"""
def longestPalindrome(s: 'str') -> 'str':
    length = 0
    result = ""
    for i in range(len(s)):
        for j in range(i,len(s)):
            if s[i:j+1] == s[i:j+1][::-1]:
                if j+1-i > length:
                    length = j+1-i
                    result = s[i:j+1]
                        
    return result
#Time complexity: O(n^3), space complexity: O(1)
                