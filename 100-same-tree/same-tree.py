# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traversalWithChecking(self, node: Optional[TreeNode], node2: Optional[TreeNode]):
        if (node != None and node2 != None and node.val == node2.val):
            return self.traversalWithChecking(node.left, node2.left) and self.traversalWithChecking(node.right, node2.right)
        elif (node == None and node2 == None):
            return True
        else:
            return False


    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.traversalWithChecking(p, q)