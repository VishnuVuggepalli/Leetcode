# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        queue = deque()
        rightView =[]

        queue.append(root)
        while queue:
            levels= []
            queueSize = len(queue)
            for _ in range(queueSize):
                temp = queue.popleft()
                levels.append(temp.val)

                if temp.left:
                    queue.append(temp.left)
                if temp.right:
                    queue.append(temp.right)
            rightView.append(levels[-1])
        return rightView