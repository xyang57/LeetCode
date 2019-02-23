"""
438. Find All Anagrams in a String
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example 1:

Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input:
s: "abab" p: "ab"

Output:
[0, 1, 2]

Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""

"""
Solution:
    first define a function for identifying anagrams. Then slide the window, and compare if the substring
    is an anagram of the other string
"""
def findAnagrams(s: str, p: str):
    result = []
    for i in range(len(s)-len(p)+1):
        new_s = s[i:i+len(p)]
        if Anagrams(new_s,p):
            result.append(i)
    return result
    
def Anagrams(s:str, p: str):
    count = {}
    for letter in s:
        try:
            count[letter] += 1
        except:
            count[letter] = 1
    for letter in p:
        if letter in count:
            count[letter] -= 1
            if count[letter] < 0:
                return False
        else:
            return False
    return True

# Time complexity: O(n^2), space complexity: O(n)
    


