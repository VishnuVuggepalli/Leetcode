# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        N = len(preorder)
        if N == 0:
            return None
        
        root = TreeNode(preorder[0])

        if N == 1:
            return root
        
        for i in range(N-1):
            if preorder[1] == postorder[i]:
                # preorder : consider window of whole left sub Tree, postorder: until leftroot
                root.left = self.constructFromPrePost(preorder[1: i+2], postorder[:i+1])

                # preorder: consider after the left sub tree postorder : consider until the last ele, whcihc is root , so omit
                root.right = self.constructFromPrePost(preorder[i + 2: ], postorder[i+1:-1])
            
                return root