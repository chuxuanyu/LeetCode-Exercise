#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 17:40:24 2018

@author: chuxuan
"""

def solution(s):
    len_ = len(s)
    results = 0
    for i in range(len(s)):
        print((ord(s[i]) -64)* (10*(len_-1)))
        results = results+((ord(s[i]) -64)* (26**(len_-1)))
        len_ -= 1
        
    return results 
        
print(solution("ZY"))        