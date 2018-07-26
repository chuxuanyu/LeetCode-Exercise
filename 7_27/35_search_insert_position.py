#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 23:13:56 2018

@author: chuxuan
"""

def searchInsert(nums, target):
    len_1 = len(nums)
    len_ = int(len_1*.5);
    
    if target == nums[len_]:
        return len_
    elif target > nums[len_]:
        while target > nums[len_]:
            len_+=1
            if len_ == len_1:
                return len_
        return len_
    else: 
        while target < nums[len_]:
            if len_ == 0:
                return 0;
            if len_ == nums[len_]:
                return len_
            if target > nums[len_-1]:
                return len_
            len_-=1
        return len_ 

print(searchInsert([1,3],1))