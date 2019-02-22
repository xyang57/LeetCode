"""
387. First Unique Character in a String
Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.

Examples:

s = "leetcode"
return 0.

s = "loveleetcode",
return 2.
Note: You may assume the string contain only lowercase letters.
"""

"""
Solution1:
    first count each character apperances with a dictionary, then iterate the dictionary and find the one
    key with only one occurance and return the index
"""
def firstUniqChar(s: 'str') -> 'int':
    dic = {}
    for letter in s:
        try:
            dic[letter] += 1
        except:
            dic[letter] = 1
    for i in range(len(s)):
        if dic[s[i]] == 1:
            return i
    return -1
# Time complexity: O(n); space complexity: O(n)