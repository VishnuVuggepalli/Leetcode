# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        
        Q = deque([root])
        
        while Q[0] is not None:
            temp = Q.popleft()
            
            Q.append(temp.left)
            Q.append(temp.right)
        while Q and Q[0] is None:
            Q.popleft()
        
        return not bool(Q)