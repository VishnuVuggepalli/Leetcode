# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        pairs = defaultdict(int)
        res =[]
        def dfs(root):
            if not root: return ''
            l,r = dfs(root.left), dfs(root.right)
            pair = f\l{l}{root.val}{r}r\
            pairs[pair] += 1
            if pairs[pair] == 2:
                res.append(root)
            return pair
        dfs(root)
        return res