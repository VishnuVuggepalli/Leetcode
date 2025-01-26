class Solution:
    def maximumInvitations(self, favorite: List[int]) -> int:
        n = len(favorite)
        inDeg = [0] * n
        chain_len = [0] * n
        visited = [False] * n
        q = deque()

        for i in favorite:
            inDeg[i] += 1
        
        for i in range(n):
            if inDeg[i] == 0:
                q.append(i)
        
        while q:
            u=q.popleft()
            visited[u] = True
            v = favorite[u]
            chain_len[v] = max(chain_len[v], chain_len[u] + 1)
            inDeg[v] -= 1
            if inDeg[v] == 0:
                q.append(v)
        
        max_cycle , pairs = 0 , 0

        for i in range(n):
            if visited[i]:
                continue
            cycle_len = 0
            current = i

            while not visited[current]:
                visited[current] = True
                current = favorite[current]
                cycle_len += 1
            if cycle_len == 2:
                pairs += 2 + chain_len[i] + chain_len[favorite[i]]
            else:
                max_cycle = max(max_cycle, cycle_len)
        return max(max_cycle, pairs)
