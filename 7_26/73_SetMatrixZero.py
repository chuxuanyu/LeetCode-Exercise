#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 19:14:27 2018

@author: chuxuan
"""

def setZeroes(matrix):
    M = len(matrix)
    N = len(matrix[0])
    record_x = []
    record_y = []
    for i in range (M):
        for j in range (N):
            if matrix[i][j] == 0:
                record_x.append(i)
                record_y.append(j)
                
    for i in record_x:
        matrix[i] = [0 for i in range(N)]
    for j in record_y:
        for i in range(M):
            matrix[i][j]=0;
    return matrix

print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]]))