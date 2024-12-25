# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        Q = deque([root])
        max_array= []
        while Q:
            level_max = float('-inf')
            for _ in range(len(Q)):
                cur = Q.popleft()
                if cur.left:
                    Q.append(cur.left)
                if cur.right:
                    Q.append(cur.right)
                level_max = max(cur.val, level_max)
            max_array.append(level_max)
        return max_array
        