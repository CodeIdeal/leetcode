# !/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


t1 = TreeNode(1)
t1l = TreeNode(3)
t1r = TreeNode(2)
t1l_l = TreeNode(5)
t1.left = t1l
t1.right = t1r
t1l.left = t1l_l

t2 = TreeNode(2)
t2l = TreeNode(1)
t2r = TreeNode(3)
t2l_r = TreeNode(4)
t2r_r = TreeNode(7)
t2.left = t2l
t2.right = t2r
t2l.right = t2l_r
t2r.right = t2r_r


class Solution:
    # @param root, a tree node
    # @return an integer
    def maxDepth(self, root):
        if root is None:
            return 0
        else:    
            return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1


a = Solution()
print(a.maxDepth(t2))