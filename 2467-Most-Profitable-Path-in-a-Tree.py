class Solution:
    def mostProfitablePath(self, edges: List[List[int]], bob: int, amount: List[int]) -> int:
        adj = defaultdict(list)
        for u,v in edges :
            adj[u].append(v)
            adj[v].append(u)
        
        # PreProcessing - simulate bob's path - analyze bob's path beforehand - bob's path os fixed ,  unlike alice's

        bob_times = {}


        def find_bob_path_dfs(src, parent, time):
            if src == 0:
                bob_times[src] = time
                return True
            for neigh in adj[src]:
                if neigh == parent:
                    continue
                if find_bob_path_dfs(neigh, src, time + 1):
                    bob_times[src] = time
                    return True
            return False
        
        find_bob_path_dfs(bob, -1, 0)



        # no Alie Simulation - find max path - use BFS to traverse to every nodes

        res = float('-inf')

        Q = deque([(0, 0, -1, amount[0])])

        while Q :
            cur_node, time, parent, count = Q.popleft()
            
            for neigh in adj[cur_node]:
                if neigh == parent:
                    continue
                neigh_profit = amount[neigh]
                neigh_time = time + 1
                if neigh in bob_times:
                    if bob_times[neigh] < neigh_time:
                        neigh_profit = 0
                    if bob_times[neigh] == neigh_time:
                        neigh_profit = neigh_profit // 2
                    

                Q.append((neigh, neigh_time, cur_node, count + neigh_profit))

                if len(adj[neigh]) == 1:
                    res = max(res, count + neigh_profit)
        
        return res