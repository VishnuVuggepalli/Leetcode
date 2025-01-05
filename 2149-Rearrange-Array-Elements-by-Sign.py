class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        eve , odd = 0, 1
        N = len(nums)
        new_arr = [0] * N
        for i in range(N):
            if nums[i] < 0:
                new_arr[odd] = nums[i]
                odd += 2
            else:
                new_arr[eve] = nums[i]
                eve += 2
        return new_arr

        # eve, odd = 0, 0
        # N = len(nums)
        # eve_arr = []
        # odd_arr = []
        # for i in range(N):
        #     if nums[i] > 0:
        #         odd_arr.append(nums[i])
        #     else:
        #         eve_arr.append(nums[i])
        # new_arr = [0] * N
        # for i in range(0,N,2):
        #     new_arr[i+1] = eve_arr[i//2]
        #     new_arr[i] = odd_arr[i//2]
        # return new_arr