#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 13:42:26 2018

@author: chuxuan
"""

def lengthOfLongestSubstring(s):
    """
    :type s: str
    :rtype: int
    """
    if len(s) == 0 or s == None:
        return 0
    else:
        dic = set()
        right = 0
        left = 0 
        results = 0
        while (right <len(s)):
            if s[right] not in dic:
                dic.add(s[right])
                right = right + 1
            else:
                results = max(right - left,results)
                while(s[left] != s[right]):
                    dic.remove(s[left])
                    left = left +1
                left = left + 1
                right = right + 1 
                
    return max(results,right-left)
                

print(lengthOfLongestSubstring("abcabcbb"))