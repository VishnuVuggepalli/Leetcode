# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def sub_tree_height(node):
            if node is None:
                return 0
            left_tree = sub_tree_height(node.left)
            right_tree = sub_tree_height(node.right)
            if left_tree < 0 or right_tree < 0 or abs(left_tree-right_tree) > 1:
                return -1
            return 1 + max(left_tree , right_tree)
        return sub_tree_height(root) >= 0