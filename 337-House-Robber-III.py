# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root is None:
                return [0,0]
            
            leftTree = dfs(root.left)
            rightTree = dfs(root.right)

            withRoot = root.val + leftTree[1] + rightTree[1]
            withoutRoot = max(leftTree) + max(rightTree)
            
            return [withRoot, withoutRoot]
        return max(dfs(root))