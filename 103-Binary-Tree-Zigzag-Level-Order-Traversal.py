# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        Q = deque()
        visited =[]

        if root is None:
            return []

        Q.append(root)

        order = True
        while Q:
            levels=[]
            qLevelSize = len(Q)
            for _ in range(qLevelSize):
                num = Q.popleft()
                levels.append(num.val)
                if num.left:
                    Q.append(num.left)
                if num.right:
                    Q.append(num.right)  
            if order:  
                visited.append(levels)
                order = False
            else:
                visited.append(levels[::-1])
                order = True

        return visited
            