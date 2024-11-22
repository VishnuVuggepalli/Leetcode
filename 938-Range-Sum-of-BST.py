# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # sum =0
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        if root.val < low:
            return self.rangeSumBST(root.right,low,high)
        elif root.val > high:
            return self.rangeSumBST(root.left,low,high)
        else: 
            return root.val + self.rangeSumBST(root.left,low,high) + self.rangeSumBST(root.right,low,high)
        # global sum
        # if root is None:
        #     return 0
        
        # self.rangeSumBST(root.left,low,high)
        # if root.val >= low and root.val <= high: self.sum += root.val 
        # self.rangeSumBST(root.right,low,high)

        # return self.sum