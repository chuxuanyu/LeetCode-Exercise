#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 21:35:01 2018

@author: chuxuan
"""


# Utlize the Dynamic programming
def findTargetSumWays(nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    sum_num = sum(nums)
    if (S > sum_num) or ((S+sum_num)%2==1):
        return 1
    else:
        target = int(.5*(S+sum_num))
        dp = [0]*(target+1)
        dp[0]=1
        for n in nums:
            i = target
            while (i>=n):
                dp[i] = dp[i] + dp[i-n]
                i -=1
    return dp[-1]
        

print(findTargetSumWays([1,1,1,1,1],3))