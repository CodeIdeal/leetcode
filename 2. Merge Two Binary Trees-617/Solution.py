#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Input: 
# 	Tree 1                     Tree 2                  
#           1                         2                             
#          / \                       / \                            
#         3   2                     1   3                        
#        /                           \   \                      
#       5                             4   7                  
# Output: 
# Merged tree:
# 	     3
# 	    / \
# 	   4   5
# 	  / \   \ 
# 	 5   4   7


# need convert to below format 
# input: a = [1,3,2,5]
# input: b = [2,1,3,null,4,null,7] 
# output: c = [3,4,5,5,4,7]


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self,old_node,new_node):
        if old_node.left == None:
            old_node.left = node
            return
        elif old_node.right == None:
            old_node.right = node
            return
        else:
            insert()



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


class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t1 == None and t2 != None:
            t = TreeNode(t2.val)
            t.left = self.mergeTrees(None,t2.left)
            t.right = self.mergeTrees(None,t2.right)
        elif t2 == None and t1 != None:
            t = TreeNode(t1.val)
            t.left = self.mergeTrees(t1.left,None)
            t.right = self.mergeTrees(t1.right,None)
        elif t1 == None and t2 == None:
            return None
        else:
            t = TreeNode(t1.val + t2.val)
            t.left = self.mergeTrees(t1.left,t2.left)
            t.right = self.mergeTrees(t1.right,t2.right)
        return t
    


class solution2(object):

    def mergeTrees(self,T1,T2):
        if not t1:
            return t2
        if not t2:
            return t1
        if t1 and t2:
            t1.val = t1.val + t2.val
            t1.left = t1.left + t2.left
            t1.right = t1.right + t2.right
            return t1s

# TODO: convert tree to array
def convert(list):
        for index,num in list:



a=[]
convert(Solution().mergeTrees(t1,t2),a)
print(a)