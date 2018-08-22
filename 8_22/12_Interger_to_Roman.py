#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 17:10:37 2018

@author: chuxuan
"""
"""
利用字典，每次减去已经表达的数字
"""
def solution(num):
    results = ""
    left = num
    roms_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    roms = {5: "V", 1: "I", 10:"X", 50: "L", 100: "C", 500:"D", 1000: "M", 4:"IV", 9:"IX", 90:"XC", 400:"CD", 900:"CM", 40:"XL"}
    
    for k in roms_list:
        while left >= k:
            results += roms[k]
            left = left - k
    return results 

print(solution(58))
