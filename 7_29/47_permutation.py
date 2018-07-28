#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 21:26:59 2018

@author: chuxuan
"""


class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        self.res = []
        sub = []
        nums = sorted(nums)
        fl = [0]*len(nums)
        self.dfs(nums,[],fl)
        return self.res

    def dfs(self, Nums, subList,flagList):
        if len(subList) == len(Nums):
            #print res,subList
            self.res.append(subList[:])
        last = None
        for idx in range(len(Nums)):
            m = Nums[idx]
            if flagList[idx]==1:
                continue
            if last == m:
                continue
            flagList[idx] = 1
            subList.append(m)
            self.dfs(Nums,subList,flagList)
            last = subList.pop()
            flagList[idx] = 0