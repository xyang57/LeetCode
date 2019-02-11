"""
58. Length of Last Wrod
Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

"""

"""
Solution: First split the string; then return the length of last element from spliting
"""
def lengthOfLastWord(s: 'str') -> 'int':
     result = s.split()
     if result:
        return len(result[-1])
     else:
        return 0
    
# Time complexity: O(n); space complexity: O(n)