#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 22:33:35 2018

@author: chuxuan
"""


class Solution(object):
    def lengthOfLIS(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums==[]:
            return 0
        
        l=len(nums)
        
        dp=[1]*l
        
        for x in range(l):
            for y in range(x):
                if nums[x]>nums[y]:
                    dp[x]=max(dp[x],dp[y]+1)
        
        return max(dp)

print(Solution.lengthOfLIS([10,9,2,5,3,7,101,18]))