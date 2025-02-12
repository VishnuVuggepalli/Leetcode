class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        max_sum = -1
        sum_idx = {}
        def digits_sum(num: int) -> int:
            res = 0
            while num >0:
                dig = num % 10
                res += dig
                num = num // 10
            return res

        for i in range(len(nums)):
            sum_of_digits = digits_sum(nums[i])
            if sum_of_digits in sum_idx:
                max_sum = max((nums[sum_idx[sum_of_digits]] + nums[i]), max_sum)
                if nums[i] > nums[sum_idx[sum_of_digits]] :
                    sum_idx[sum_of_digits] = i
            else:
                sum_idx[sum_of_digits] = i
        return max_sum