"""
20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true
Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
"""

""" 
Use stack to solve this problem; If the current letter is a left bracket,
push in stack; if the current letter is a right bracket: if the stack is empty,
return false, else pop out the last element in stack and check if the two brackets
match; in the end check if the stack is empty
"""
def isValid(s: 'str') -> 'bool':
    dic = {')':'(',
           '}':'{',
           ']':'['}
    result = []
    for letter in s:
        if letter not in dic:
            result.append(letter)
        else:
            if len(result) == 0:
                return False
            a = result.pop()
            if a != dic[letter]:
                return False
    return not result

# Time complexity: O(n); Space complexity: O(n)