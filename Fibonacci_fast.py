#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 01:27:21 2018

@author: xuyang
"""

def climbStairs(n, memo = {}):
    """
    :type n: int
    :rtype: int
    """
        
    if n==0 or n==1:
        return 1
    try:
        return memo[n]
    except KeyError:
        result = climbStairs(n-1, memo) + climbStairs(n-2, memo)
        memo[n] = result
        return result