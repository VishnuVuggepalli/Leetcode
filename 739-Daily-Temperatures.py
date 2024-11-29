class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans =[0] * len(temperatures)
        stack = []
        for day in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[day]:
                old_day = stack.pop()
                ans[old_day] = day - old_day
            stack.append(day)
        return ans