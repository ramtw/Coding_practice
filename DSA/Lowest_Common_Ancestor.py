# Problem Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# Method-1
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        ans=TreeNode(0)
        def fun(node):
            nonlocal ans
            if(node==None):
                return 0
            c=0
            if(node==p or node==q):
                c=1
            c= c+fun(node.left)+fun(node.right)
            if(c==2):
                ans=node
                return -1
            return c
        x=fun(root)
        return ans

# Method-2
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root or root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root

        return left or right        
