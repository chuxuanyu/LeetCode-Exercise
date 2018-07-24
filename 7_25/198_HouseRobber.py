#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 20:51:42 2018

@author: chuxuan
"""
# dynamic programming: 
# should take care of the the specific issue such as len_ = 0, 1 and 2.
def rob(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    len_ = len(nums)
    dp = [0]*len_
    if len_ == 0:
        return 0
    elif len_ == 1:
        return nums[0]
    elif len_ == 2:
        return max(nums[0],nums[1])
    else:
        dp[0] = nums[0]
        dp[1] = max(nums[0],nums[1])
        for i in range(2,len(nums),1):
            dp[i] = max(dp[i-1],dp[i-2]+nums[i])
    return dp[-1]

print(rob([2,7,9,3,1]))