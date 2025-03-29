class Solution:
    def canJump(self, nums: List[int]) -> bool:
        '''
        happy case  if i has reached len(nums) -1 
        '''

        # @lru_cache
        # def validate_jumps(i : int):
        #     #happy_case
        #     # print(i)
        #     if i > len(nums) -1 :
        #         return False
        #     if i + nums[i] == len(nums)-1:
        #         return True
        #     for j in range(1,nums[i]+1):
        #         if validate_jumps(i+j):
        #             return True
        #     return False
        # return validate_jumps(0)

        reach = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if i + nums[i] >= reach:
                reach = i
        return reach == 0