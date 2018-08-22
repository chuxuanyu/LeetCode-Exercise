#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 20:39:42 2018

@author: chuxuan
"""

def solution(num,target):
    nums = sorted(num)
    curr = nums[0] +nums[1] +nums[-1]
    for i in range(len(nums)-2):
        if i>0 and nums[i] == nums[i-1]:
            continue
        l = i +1
        r = len(nums)-1
        while l<r:
            val = nums[i] + nums[l] + nums[r]
            if abs(val-target) <abs(curr-target):
                curr = val
            if val == target:
                return val
            if val <target:
                l += 1
            else:
                r -= 1
    return curr

            
            
    
    