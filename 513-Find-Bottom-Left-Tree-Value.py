# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        Q = collections.deque()
        Q.append(root)

        res =[]
        while Q:
            size_of_Q = len(Q)
            level = []
            for _ in range(size_of_Q):
                current = Q.popleft()
                if current.left : Q.append(current.left)
                if current.right : Q.append(current.right)
                level.append(current.val)
            res.append(level[0])
        
        return res[-1]