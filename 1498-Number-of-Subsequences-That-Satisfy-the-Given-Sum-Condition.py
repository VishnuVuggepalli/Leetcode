class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        count = 0
        left = 0
        modulo = 10 **9 + 7
        right = len(nums) -1
        while left <= right:
            if nums[left] + nums[right] > target:
                right -=1
            else:
                count += pow(2, right -left, modulo)
                left += 1
        return count % modulo
        # nums.sort()
        # no_dups = set()
        # count = 0
        # modulo = 1000000007
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] + nums[j] > target:
        #             temp = nums[i:j+1]
        #             no_dups.add(tuple(temp))
        #             count += 1
        # print(no_dups)
        # return (2 ** len(nums) % modulo) - count