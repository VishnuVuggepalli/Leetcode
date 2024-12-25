# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        '''
        1. BFS -if the answer is found near - suggested
        2. DFS - found in the leaf of the tree - suggested
        '''

        def sort_level(arr):
            count = 0
            idx_map = {n:i for i , n in enumerate(arr)}
            sorted_arr = sorted(arr)
            for i in range(len(arr)):
                if arr[i] != sorted_arr[i]:
                    count+= 1
                    j = idx_map[sorted_arr[i]]
                    arr[i], arr[j] = arr[j], arr[i]
                    idx_map[arr[j]] = j
            return count
    
        Q = deque([root])
        change_count =0
        while Q:
            level = []
            for _ in range(len(Q)):
                cur = Q.popleft()
                if cur.left:
                    Q.append(cur.left)
                if cur.right:
                    Q.append(cur.right)
                level.append(cur.val)
            change_count += sort_level(level)
        return change_count