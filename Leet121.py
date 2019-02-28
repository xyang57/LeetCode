"""
Leet 121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

"""
Solution1:
    Brute force: try every possible combinations
"""
def maxProfit(prices):
    max_profit = 0
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            profit = prices[j] - prices[i]
            if profit > max_profit:
                max_profit = profit
    return max_profit

# Time complexity: O(n^2); space complexity: O(1)

"""
Solution2:
    Find identify the minimum value, then keep updating the max profit
"""
def maxProfit(prices):
    if len(prices) == 0:
        return 0
    max_profit = 0 # Initialize max_profit to be 0 
    valley = prices[0] # Initialize the valley to be the first price
    for i in range(1,len(prices)):
        if prices[i] < valley:
            valley = prices[i]
        max_profit = max(max_profit, prices[i] - valley)       
    return max_profit

# Time complexity: O(n); space complexity: O(1)
    
    