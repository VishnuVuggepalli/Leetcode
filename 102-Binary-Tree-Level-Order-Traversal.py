# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = [root]
        visited = []

        while queue:
            level_size = len(queue)
            level = []
            for i in range(level_size):
                tempRoot = queue.pop(0)
                level.append(tempRoot.val)
                if tempRoot.left:
                    queue.append(tempRoot.left)
                if tempRoot.right:
                    queue.append(tempRoot.right)
            visited.append(level)
        return visited