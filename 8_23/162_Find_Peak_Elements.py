#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 21:31:26 2018

@author: chuxuan
"""
"""
Method 1: 
"""
class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == None:
            return None
        if len(nums) == 1 or nums[0] > nums[1]:
            return 0
        if nums[-1] > nums[-2]:
            return len(nums)-1
        
        for i in range(1,len(nums)-1):
            if nums[i] > nums[i-1]:
                if nums[i] > nums[i+1]:
                    return i
                