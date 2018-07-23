#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 20:24:37 2018

@author: chuxuan
"""
# My Own Idea
def countBits(num):
    results = [0 for i in range(num+1)]
    for i in range (num+1):
        n = i
        while n:
            results[i] = results[i] + (n & 1)
            n >>= 1
    return results

# 一个查1个数的方程 bin(num).count('1')， 但是不符合追踪   
# 将其拆分成【0-1】【2-3】【4-7】等：
def countBits1( num):
    dp = [0]
    i = 0
    while True:
        for j in range(1<<i, 1<<(i+1)):
            if j > num:
                return dp
            dp.append(1 + dp[j - (1<<i)])
        i += 1
    return dp
#
def countBits2(num):
    dp = [0];
    for i in range(1,num+1):
        dp.append(dp[i>>1] + (i&1))
    return dp

if __name__ == '__main__':
    result = countBits(15)
    result1 = countBits1(15)
    result2 = countBits2(15)