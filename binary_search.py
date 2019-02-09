#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 20:04:29 2018

@author: xuyang
"""

def binary_search(input_array, value):
    """
    :type input_array: array
    :type value: interger
    :rtype: an index for the value, if not in array, return -1
    """
    low = 0
    high = len(input_array) - 1
    while (low <= high):
        mid = (low + high)//2
        if input_array[mid] == value:
            return mid
        elif input_array[mid] > value:
            high = mid - 1
        else: 
            low = mid + 1
    return -1