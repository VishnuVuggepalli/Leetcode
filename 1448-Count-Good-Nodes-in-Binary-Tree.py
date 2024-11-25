# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, maxVal):
            if root is None:
                return 0
            if root.val >= maxVal:
                count =1
            else:
                count =0
            maxVal = max(maxVal, root.val)
            return count + dfs(root.left, maxVal) + dfs(root.right, maxVal)
        return dfs(root, float('-inf'))