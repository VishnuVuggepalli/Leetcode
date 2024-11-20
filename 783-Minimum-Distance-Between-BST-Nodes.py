# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    mini = float('inf')
    prev = None
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        def inOrder(root):
            if root.left:
                self.minDiffInBST(root.left)
            if self.prev:
                if abs(root.val - self.prev.val) < self.mini:
                    self.mini = root.val - self.prev.val
            self.prev = root
            if root.right:
                self.minDiffInBST(root.right)
        inOrder(root)
        return self.mini

        