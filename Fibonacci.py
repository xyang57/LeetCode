#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 30 21:04:59 2018

@author: xuyang
"""

def fib(position):
    if position == 1 or position == 0:
        return position
    return fib(position - 1) + fib(position - 2)