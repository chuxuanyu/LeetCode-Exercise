#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 17:56:30 2018

@author: chuxuan
"""

def pluseone(digits):
    
    for i in range(len(digits)-1,-1,-1):
        if digits[i] == 9 and i != 0:
            digits[i] = 0
        elif digits[i] == 9 and i == 0:
            digits[i] = 0
            digits.insert(0,1)
            return digits
        else:
            digits[i] = digits[i] + 1
            return digits
    return digits
print(pluseone([1,7]))