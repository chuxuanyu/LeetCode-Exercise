#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 22:06:12 2018

@author: chuxuan
"""

def moveZeroes(nums):
    """
    :type nums: List[int]
    :rtype: void Do not return anything, modify nums in-place instead.
    """
    j = 0
    
    for i in range(len(nums)):
        if nums[i] == 0:
            j = j+1
        if nums[i]!=0:
            nums[i-j] =nums[i]
    for i in range(j):
        p = len(nums)-i-1
        nums[p]=0
    return nums

def moveZeroe(nums):
    zero = 0  # records the position of "0"
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    return nums
