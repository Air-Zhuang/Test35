"""
深度优先遍历二叉树(先(根)序遍历)
"""

class BinTreeNode:
    def __init__(self,data,left=None,right=None):
        self.data,self.left,self.right=data,left,right

class BinTree:
    def __init__(self,root):
        self.root=root

    def preorder_trav(self,subtree):    #先(根)序遍历
        if subtree:
            print(subtree.data)
            self.preorder_trav(subtree.left)
            self.preorder_trav(subtree.right)

a=BinTreeNode(111,None,None)
b=BinTreeNode(333,None,None)
root=BinTreeNode(222,a,b)

b=BinTree(root)
b.preorder_trav(b.root)

"""
左右反转二叉树
https://leetcode.com/problems/invert-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left,root.right=root.right,root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

"""
广度优先遍历二叉树(层序遍历)
"""
