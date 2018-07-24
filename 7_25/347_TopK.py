#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 21:11:32 2018

@author: chuxuan
"""
# bucket algorithm
def topKFrequent(nums, k):
    data, res = {},[]
    for i in nums:
        data[i] = data[i] + 1 if i in data else 1
    bucket = [[] for i in range(len(nums)+1)]
    for key in data:
        bucket[data[key]].append(key)
    for i in range(len(bucket)-1,-1,-1):
        if bucket[i]:
            res.extend(bucket[i])
        if len(res)>= k:
            break
    return res[:k]

print(topKFrequent([8,8,8,9,9,9,7], 2))
