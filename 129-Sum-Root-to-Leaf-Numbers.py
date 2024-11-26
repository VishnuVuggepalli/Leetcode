# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        strArray =[]
        def findPair(root,s):
            if root is None:
                return 0
            s += str(root.val)
            if not root.left and not root.right:
                strArray.append(s)
            findPair(root.left, s)
            findPair(root.right,s)
            return root
        findPair(root,s = '')
        print(strArray)
        return sum(int(x) for x in strArray)