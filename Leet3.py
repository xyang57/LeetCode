"""
3. Longest Substring Without Repeating Characters
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3 
Explanation: The answer is "abc", with the length of 3. 
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3. 
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
Solution1:
    Find the maximum length of each substring starting with each index, and then return the longest
"""
def lengthOfLongestSubstring(s: 'str') -> 'int':
    length_maximum = 0 # Initiate the maximum length
    for i in range(len(s)):
        length = 0 # For each starting index, initiate the length to 0
        substring = set() # with set we can search with constant time
        for j in range(i,len(s)):
            if s[j] not in substring: 
                length += 1
                substring.add(s[j])
                length_maximum = max(length,length_maximum)
            else:
                break   
    return length_maximum
# Time complexity: O(n^2), space complexity: O(n)
    
"""
Solution2: if we find a duplicate value, then we can cut off the original string to replicated index +1, 
and continue to iterate through the string
"""

def lengthOfLongestSubstring(s: 'str') -> 'int':
    length_maximum = 0
    sub = ''
    for i in range(len(s)):
        if s[i] not in sub:
            sub+=s[i]
            length_maximum = max(length_maximum, len(sub))
        else:
            index = sub.index(s[i])
            sub = sub[index+1:]+s[i]
    return length_maximum

# Time complexity: O(n^2), because *in* is O(n); space complexity: O(n)