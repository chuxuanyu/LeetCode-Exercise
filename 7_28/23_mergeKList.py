#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 23:54:54 2018

@author: chuxuan
"""

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        resmap = {}
        for list in lists:
            while list != None:
                # print(list.val)
                if list.val in resmap:
                    resmap[list.val] += 1
                else:
                    resmap[list.val] = 1
                list = list.next
                    
        # sorted(resmap)
        
        res = ListNode(-1)
        result = res
        for key in sorted(resmap.keys()):
            for _ in range(resmap[key]):
                # print('The value: ', key)
                res.next = ListNode(key)
                res = res.next
        return result.next