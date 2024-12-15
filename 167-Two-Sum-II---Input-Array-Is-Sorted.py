class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        for idx,num in enumerate(numbers):
            if num not in visited:
                visited[num] = idx + 1
            if target-num in visited and visited[target-num] != idx+1:
                return [visited[target-num], idx+1]
        