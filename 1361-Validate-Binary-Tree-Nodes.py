class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        root =0
        child = set(leftChild + rightChild)
        for i in range(n):
            if i not in child:
                root =i

        visited = set()
        Q = collections.deque([root])

        while Q:
            node = Q.popleft()
            if node in visited:
                return False
            visited.add(node) 
            if leftChild[node] != -1:
                Q.append(leftChild[node])
            if rightChild[node] != -1:
                Q.append(rightChild[node])
        
        return len(visited) == n