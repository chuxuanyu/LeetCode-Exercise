#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 18:25:41 2018

@author: chuxuan
"""

def numIslands(grid):
    """
    :type grid: List[List[str]]
    :rtype: int
    """
    result = 0;
    if not grid:
        return 0
    for a in range(len(grid)):
        for b in range(len(grid[0])):
            if grid[a][b] == '1':
                dfs(grid,a,b)
                result = result +1
    return result
def dfs(grid,i,j):
    if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] != '1':
        return 
    grid[i][j] = '0'
    dfs(grid,i+1,j)
    dfs(grid,i-1,j)
    dfs(grid,i,j+1)
    dfs(grid,i,j-1)

print(numIslands[["1","0"],["1","0"]])
        


    