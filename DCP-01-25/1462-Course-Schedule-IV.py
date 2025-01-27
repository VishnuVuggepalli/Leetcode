class Solution:
    def checkIfPrerequisite(self, n: int, p: List[List[int]], qu: List[List[int]]) -> List[bool]:
        adj= [[] for _ in range(n)]
        inDeg = [0] * n
        for pre, cur in p:
            adj[pre].append(cur)
            inDeg[cur] += 1

        q = deque()

        for i in range(n):
            if inDeg[i] == 0:
                q.append(i)
        
        indirectMap = defaultdict(set)

        while q:
            cur = q.popleft()
            for cont in adj[cur]:
                indirectMap[cont].add(cur)
                indirectMap[cont].update(indirectMap[cur])
                inDeg[cont] -= 1
                if inDeg[cont] == 0:
                    q.append(cont)
        
        return [u in indirectMap[v] for u,v in qu]

        # graph = defaultdict(list)

        # for preq, course in p:
        #     graph[course].append(preq)

        
        # def dfs(course):
        #     if course not in indirectMap:
        #         indirectMap[course] = set()
        #         for pre in graph[course]:
        #             indirectMap[course] |= dfs(pre)
        #         indirectMap[course].add(course)
        #     return indirectMap[course]
        

        # indirectMap ={}
        # for index in range(n):
        #     dfs(index)
        # print(indirectMap)

        # res = []
        # for u , v in q:
        #     res.append(u in indirectMap[v])
        # return res