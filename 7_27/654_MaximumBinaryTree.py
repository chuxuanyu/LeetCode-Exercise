#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 21:36:05 2018

@author: chuxuan
"""
class TreeNode(object):
    def __init__(self,x):
        self.val=x
        self.left=None
        self.right=None

def constructMaximumBinaryTree(nums):
    def getsubtree(nums,start,end):
        if start == end :
            return None
        max_ = max(nums[start:end])
        node = TreeNode(max_)
        node.left = getsubtree(nums,start,nums.index(max_))
        node.right = getsubtree(nums,nums.index(max_)+1,end)
        return node
    return getsubtree(nums,0,len(nums))

print (constructMaximumBinaryTree([3,2,1,6,0,5]))
