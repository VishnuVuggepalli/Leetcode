class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        self.initArray = [-1] * (len(edges) +1)

        def find(x):
            while self.initArray[x] > 0:
                x = self.initArray[x]
            return x
        
        def union(x,y):
            nx = find(x)
            ny = find(y)
            
            if nx == ny:
                return False
            else:
                self.initArray[nx] = ny
                return True
        
        for u,v in edges:
            if not union(u,v):
                return [u,v]
        # adj = {}
        # for u,v in edges:
        #     if u not in adj:
        #         adj[u] = []
        #     adj[u].append(v)
        #     if v not in adj:
        #         adj[v] = []
        #     adj[v].append(u)
        
        # print(adj)
        # for u,v in reversed(edges):
        #     if len(adj[v]) > 1:
        #         return [u,v]
            
        # return []