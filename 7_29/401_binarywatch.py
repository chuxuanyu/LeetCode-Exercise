#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 23:08:35 2018

@author: chuxuan
"""

def readBinaryWatch(num):
    """
    :type num: int
    :rtype: List[str]
    """
    res = []
    for h in range(12):
        for m in range(60):
            if (bin(h)+bin(m)).count('1') == num:
                res.append('%d:%02d' % (h, m))
    return res
print(readBinaryWatch(1))