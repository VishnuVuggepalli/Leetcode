# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        def isSame(p, q):
            if not p and not q: return True
            if not p or not q or p.val != q.val: return False

            return isSame(p.left, q.right) and isSame(p.right, q.left)

        return isSame(root.left, root.right)

        # Q = deque()
        # visited = []
        
        # Q.append(root)

        # while Q:
        #     levels= []
        #     for i in range(len(Q)):
        #         temp = Q.popleft()
        #         visited.append(temp.val)
        #         if temp.left :
        #             Q.append(temp.left)
        #         if temp.right:
        #             Q.append(temp.right)
        #         levels.append(temp)
        #     print(levels)
        #     if levels != levels[::-1]:
        #         return False
        # return True
            