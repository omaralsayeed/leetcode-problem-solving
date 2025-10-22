# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def swap(self, node: Optional[TreeNode]):
        if (node != None):
            temp = node.right
            node.right = node.left
            node.left = temp
            if (node.right != None):
                self.swap(node.right)
            if (node.left != None):
                self.swap(node.left)

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.swap(root)
        return root      