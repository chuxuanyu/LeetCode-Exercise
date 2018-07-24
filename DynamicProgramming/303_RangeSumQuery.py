#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 23:22:49 2018

@author: chuxuan
"""

def sum_(nums):
    sumNums = [0 for i in range(len(nums)+1)]
    for i in range(len(nums)):
        sumNums[i+1] = sumNums[i] + nums[i]
    return sumNums

def sumRange(sumNums,i,j):
    return(sumNums[j+1]-sumNums[i])
    
sum__=sum_([-2, 0, 3, -5, 2, -1])
print(sumRange(sum__,1,2))
    