# Problem Link: https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    mp={}
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if(node==None):
            return None
        n=Node(node.val)
        self.mp[node]=n
        for neighbor in node.neighbors:
            if(neighbor in self.mp):
                n.neighbors.append(self.mp[neighbor])
            else:
                n.neighbors.append(self.cloneGraph(neighbor))
        return n 
