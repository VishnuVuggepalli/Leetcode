class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(idx:int, cur_arr: list, cur_sum:int ):
            if cur_sum > target:
                return
            if target == cur_sum:
                res.append(cur_arr[:])
                return
            
            for i in range(idx, len(candidates)):
                cur_arr.append(candidates[i])
                backtrack(i, cur_arr, cur_sum + candidates[i])
                cur_arr.pop()

        backtrack(0,[], 0)

        return res
            