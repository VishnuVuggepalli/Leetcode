class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums[0])
        res = []
        binary_arr = ["0", "1"]

        def backtrack(index, cur_arr):
            if len(cur_arr) > N or len(res) != 0 or index >= len(binary_arr) :
                return
            if len(cur_arr) == N:
                temp = "".join(cur_arr)
                if temp not in nums: res.append(temp)
            
            cur_arr.append(binary_arr[index])
            backtrack(index, cur_arr)
            cur_arr.pop()
            backtrack(index+1, cur_arr)

        backtrack(0, [])
        return res[0]