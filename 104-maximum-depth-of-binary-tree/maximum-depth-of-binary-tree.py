from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def calcDepth(self, node: Optional[TreeNode]) -> int:
        if (node == None):
            return 0
        else:
            return 1 + max([self.calcDepth(node.left), self.calcDepth(node.right)])
       
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.calcDepth(root)
        