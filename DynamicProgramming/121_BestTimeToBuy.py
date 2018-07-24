#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 00:06:49 2018

@author: chuxuan
"""

def maxProfit(prices):
    min_ = [0 for i in range(len(prices))]
    min_[0] = prices[0];
    diff = 0;
    if len(prices) >=2:       
        min_[1] = min(prices[1],prices[0])
        diff = diff = max(diff,prices[1]-min_[1])
        for i in range(2,len(prices)):
            min_[i] = min(min_[i-1],prices[i])
            diff = max(diff,prices[i]-min_[i])
    return diff

print(maxProfit([7,1,5,3,6,4]))
