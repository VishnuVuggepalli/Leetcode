# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertBT(self, levels:dict, traversal:str, index:int):
        while index < len(traversal):
            depth = 0
            while index < len(traversal) and traversal[index] == '-':
                depth += 1
                index += 1
            num = 0
            while index < len(traversal) and traversal[index].isdigit():
                num = num * 10 + int(traversal[index])
                index += 1

            # find parent
            parent_node = levels[depth-1]

            # make cur num node
            cur_node = TreeNode(num)

            # place node in map 
            levels[depth] = cur_node

            # connect nodes
            if parent_node.left is None:
                parent_node.left =  cur_node
            else:
                parent_node.right = cur_node
        
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        levels = {}
        num = 0
        char = 0
        while char < len(traversal) and traversal[char].isdigit():
            num = num * 10 + int(traversal[char])
            char += 1
        levels[0] = TreeNode(num)

        self.insertBT(levels, traversal, char)

        return levels[0]