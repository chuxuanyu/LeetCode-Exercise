#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 28 15:36:04 2018

@author: chuxuan
"""

graph = {"A":["B","C"],
         "B":["A","C","D"],
         "C":["A","B","D","E"],
         "D":["B","C","E","F"],
         "E":["C","D"],
         "F":["D"]}

def BDFS(graph,s):
    queue = []
    queue.append(s)
    seen = set() # 不重复的集合
    seen.add(s)
    while(len(queue)>0):
        vertex = queue.pop() # dpf: pop() take the last one bfs: pop(0) take the first one
        nodes = graph[vertex]
        for i in nodes:
            if i not in seen:
                seen.add(i)
                queue.append(i)
        print(vertex)

print(BDFS(graph,"A"))

