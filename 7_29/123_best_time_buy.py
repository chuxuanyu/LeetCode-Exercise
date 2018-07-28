#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 23:22:35 2018

@author: chuxuan
"""

import sys
class Solution:
    def maxProfit(prices):
        r=0
        l=len(prices)
        if l<=1:
            return 0
        start=[0]*(l+1)
        end=[0]*(l+1)
        i=l-1
        maxp=prices[-1]
        while i>=0:
            if prices[i]<maxp:
                start[i]=max(start[i+1],maxp-prices[i])
            elif prices[i]>=maxp:
                start[i]=start[i+1]
                maxp=prices[i]
            i-=1
        #print(start)
        minp=prices[0]
        i=1
        while i<l:
            if prices[i]>minp:
                end[i]=max(end[i-1],prices[i]-minp)
            elif prices[i]<=minp:
                end[i]=end[i-1]
                minp=prices[i]
            i+=1
        #print(end)
        r=0
        for i in range(l):
            if start[i+1]+end[i]>r:
                r=start[i+1]+end[i]
        return r

Solution.maxProfit([3,3,5,0,0,3,1,4])