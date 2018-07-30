#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 30 10:21:23 2018

@author: chuxuan
"""

  
def leastInterval(tasks, n):
    hm = {}
    for t in tasks:
        if t not in hm:
            hm[t] = 1
        else:
            hm[t]+= 1
    
    m = 0   # max task frequency
    mc = 1   # num tasks at that max frequency
    for v in hm.values():
        if v == m:
            mc += 1
        elif v > m:
            mc = 1
            m = v         

    base = m*mc # count of all max frequency tasks
    base += (m-1)*(n-(mc-1)) # add in the "spacer" elements
   
    return max(base, len(tasks))
				
print(leastInterval(["A","B","C","D","E","A","B","C","D","E"],6))




