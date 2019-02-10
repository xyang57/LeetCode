"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.
"""

"""
First solution:
    sort two strings and then compare if they're the same
"""
def isAnagram(self, s: 'str', t: 'str') -> 'bool':
    return sorted(s) == sorted(t)

# Time complexity: O(nlogn): sort, O(nlogn); comparison: O(n); space  complexity:O(1)
    

"""
Second solution:
    using hash table to store the first string, and then minus if the same letter
    appears, if second string letter not in hash table, reutrn false
"""
def isAnagram(self, s: 'str', t: 'str') -> 'bool':
    if len(s)!=len(t):
        return False
    dic = {}
    for letter in s:
        if letter not in dic:
            dic[letter] = 1
        else:
            dic[letter] += 1
    for letter in t:
        if letter not in dic:
            return False
        else:
            dic[letter] -= 1
            if dic[letter] < 0:
                return False
    for y in dic.values():
        if y > 0:
            return False
    return True

#Time complexity: O(n), space complexity:O(1)

