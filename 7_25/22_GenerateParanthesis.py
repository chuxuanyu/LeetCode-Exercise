#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 24 22:18:53 2018

@author: chuxuan
"""
   


def gengeratePar(n):
    res =[]
    generate(n,n,"",res)
    return res

def generate(left,right,str,res):
    if left == 0 and right == 0:
        res.append(str)
        return 
    if left > 0:
        generate(left-1,right,str +'(',res)
    if  right > left:
        generate(left,right-1,str+')',res)
    
print(generateParenthesis(3))           