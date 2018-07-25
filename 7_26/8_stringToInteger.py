#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:54:27 2018

@author: chuxuan
"""
# use the re library to find the str
# {0,1} the number of str before that can exist
# [0-9]+ the + means that the str can repeat
def myAtoi(str):
    if not str:
        return 0
    int_max = 2**31-1
    int_min = -2**31
    import re 
    
    newstr=""
    match = re.search("^[+-]{0,1}[0-9]+",str.strip())
    
    if match:
        newstr = int(match.group())
        if (int_min < newstr < int_max):
            return newstr
        else:
            if newstr <=int_min:
                return int_min
            else:
                return int_max
                
    return match

print(myAtoi("42"))