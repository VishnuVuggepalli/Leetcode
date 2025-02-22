class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Q = deque()
        max_array = []

        for i in range(k):
            while Q and nums[i] > Q[-1]:
                Q.pop()
            Q.append(nums[i])

        max_array.append(Q[0])

        for i in range(k, len(nums)):
            if Q[0] == nums[i-k]:
                Q.popleft()
            while Q and nums[i] > Q[-1]:
                Q.pop()
            Q.append(nums[i])
            max_array.append(Q[0])
        
        return max_array