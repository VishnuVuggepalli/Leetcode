class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        colors = defaultdict(int)
        visited = {}
        res = []
        for i, color in queries:
            if i not in visited:
                visited[i] = color
            else:
                if colors[visited[i]] == 1:
                    del colors[visited[i]]
                else:
                    colors[visited[i]] -= 1
                visited[i] = color
            colors[color] += 1
            res.append(len(colors))
        
        return res
            