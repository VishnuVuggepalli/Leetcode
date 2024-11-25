# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxCount =0
        Q = collections.deque(([(root, 0)]))

        while Q:
            sizeOfQ = len(Q)
            _, startIndexofLevel = Q[0] 
            for i in range(sizeOfQ):
                vertex, idx = Q.popleft()
                if vertex.left:
                    Q.append((vertex.left, 2*idx +1))
                if vertex.right:
                    Q.append((vertex.right, 2*idx +2))
            maxCount= max(maxCount, idx - startIndexofLevel +1)
        return maxCount