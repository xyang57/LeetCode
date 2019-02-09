#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:20:44 2018

@author: xuyang
"""

def bubblesort(array):
    """
    :type array: array
    :rtype: sorted array
    """
    swap = False
    while not swap:
        swap = True
        for i in range(len(array) - 1):
            if array[i + 1] < array[i]:
                swap = False
                temp = array[i + 1]
                array[i + 1] = array[i]
                array[i] = temp
    return array

def selectionSort(array):
    """
    :type array: array
    :rtype: sorted array
    """
    for i in range(len(array)):
        for j in range(i, len(array)):
            if array[i] > array[j]:
                array[i],array[j] = array[j], array[i]
    return array

def merge(left, right):
    """
    :type left: sorted array
    :type right: sorted array
    :rtype: sorted array
    """
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else: 
            result.append(right[j])
            j += 1
    while i < len(left):
        result.append(left[i])
        i += 1
    while j < len(right):
        result.append(right[j])
        j += 1
    return result

def mergeSort(array):
    """
    :type array: array
    :rtype: sorted array
    """
    if len(array) < 2:
        return array[:]
    else:
        middle = len(array)//2
        left = mergeSort(array[:middle])
        right = mergeSort(array[middle:])
        return merge(left, right)

def quickSort(array):
    """
    :type array: array
    :rtype: sorted array
    """
    if len(array) < 2:
        return array[:]
    smaller, equal, larger = [], [], []
    pivot = array[len(array)-1]
    for num in array:
        if num < pivot:
            smaller.append(num)
        elif num == pivot:
            equal.append(num)
        else:
            larger.append(num)
    return quickSort(smaller) + equal + quickSort(larger)

def partition(a, low, high):
    """
    :type a: array
    :type low: interger representing start index for array a 
    :type high: interger representing end index for array a
    :rtype: interger representing where the pivot should be
    """
    i = low - 1
    pivot = a[high] #set the pivot the end of wanted array
    for j in range(low, high):
        if a[j] <= pivot:
            i += 1
            a[i], a[j] = a[j], a[i]
    a[i+1],a[high] = a[high],a[i+1]
    return i+1

def quicksort_inplace(a, low = 0, high=None):
    """
    :type a: array
    :type low: interger representing start index for array a
    :type high: interger representing end index for array a
    :rtype: sorted array in place
    """
    if high == None:
        high = len(a) - 1
    if low < high:
        p_idx = partition(a, low, high)
        quicksort_inplace(a,low,p_idx-1)
        quicksort_inplace(a,p_idx+1,high)

    














