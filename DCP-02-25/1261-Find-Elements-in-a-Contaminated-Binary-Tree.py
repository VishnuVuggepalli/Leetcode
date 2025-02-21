# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen = set()
        root.val = 0
        self.decontaminate(root)

    def decontaminate(self, node: Optional[TreeNode]):
        
        if node is None:
            return      
        self.seen.add(node.val)
        if node.left:
            node.left.val = (node.val * 2) + 1
            self.decontaminate(node.left)
        if node.right:
            node.right.val = (node.val * 2) + 2
            self.decontaminate(node.right)
        
    def find(self, target: int) -> bool:
        return True if target in self.seen else False

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)