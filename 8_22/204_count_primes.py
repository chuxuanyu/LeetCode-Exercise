#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 16:09:22 2018

@author: chuxuan
"""

def eratosthenes(n):
    IsPrime = [True] * (n + 1)
    IsPrime[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if IsPrime[i]:
            for j in range(i * 2, n + 1, i):
                IsPrime[j] = False
    a ={x for x in range(2, n + 1) if IsPrime[x]}
    return (len(a))

"""
求质数：
1. 利用埃拉托斯特尼筛法 将倍数全部删除。
2. 范围是【2，sqr(n)】

"""

def countPrimes(n):
    if n < 2:
        return 0
    
    IsPrimes = [1]*n
    IsPrimes[0]=IsPrimes[1] = 0
    
    for i in range (2,n,1):
        if IsPrimes[i]:
            IsPrimes[i*i:n:i] = [0] * int((n-i*i-1)/i +1)
    return (sum(IsPrimes))
                
if __name__ == "__main__":
    print (eratosthenes(20))
    print (countPrimes(20))
                    