#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 22 23:56:46 2018

@author: chuxuan
"""    

# My Own Idea 
def reverse_bit(n):
    binary = [0 for i in range(32)]
    final = 0;
    
    for i in range(31,-1,-1):
        if n == 2**i or n > 2**i:
            binary[i] = 1
            n = n -2**i
            
    for i in range(0,32,1):
        final = final + (binary[i])*(2**(31-i))
    
    return final            
           
# In fact, integers are binary in Python:
def Reverse_Bit(num):
    result = 0
    numOfBits = 32
    for i in range (numOfBits):
        result = (result << 1) +(num & 1) 
        num >>= 1
    return result 

if __name__ == '__main__':
    final = Reverse_Bit(43261596)
    final2 = reverse_bit(43261596)
     


    