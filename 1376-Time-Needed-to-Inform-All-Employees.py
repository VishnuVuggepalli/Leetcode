class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        superiorityLevels = collections.defaultdict(list)
        for i in range(n):
            superiorityLevels[manager[i]].append(i)
        Q = deque([(headID,0)])
        maxCount = 0
        while Q:
            lev,time = Q.popleft()
            maxCount = max(maxCount,time)
            for i in superiorityLevels[lev]:
                Q.append((i, time+informTime[lev]))
        return maxCount

