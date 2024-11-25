# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, lower, higher):
            if root is None:
                return True
            if not lower < root.val < higher:
                return False
            return dfs(root.left, lower, root.val) and dfs(root.right, root.val, higher)
        return dfs(root, float('-inf'), float('inf') )