"""
70. Climbing Stairs
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""

"""
Solution1:
    This problem is the same as Fibonacci Number: Fib(n) = Fib(n-1) + Fib(n-2)
"""
def climbStairs('int') -> 'int':
    if n == 1:
        return 1
    first = 1
    second = 2
    if n >= 3:
        for i in range(3,n+1):
            third = first + second
            first = second
            second = third
    return second
# Time complexity: O(n); space complexity: O(1)
    
