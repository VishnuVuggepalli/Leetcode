class Solution:
    def findMaxLength(self, nums: List[int]) -> int:

        max_len = 0
        max_index ={}
        prefix =0
        for i in range(len(nums)):
            prefix += 1 if nums[i] == 1 else -1

            if prefix == 0:
                max_len = i + 1
            elif prefix in max_index :
                max_len = max(max_len ,i - max_index[prefix])
            else:
                max_index[prefix] = i
        return max_len

        # max_contiguous_len = 0
        # left, right = 0 , 1
        # count_map= [0]*len(nums)

        # for i in range(len(nums)):
        #     if i == 1:
        #         count_map[0] += 1
        #     elif i == 0:
        #         if count_map[i] != 0:
        #             count_map[1] += 1
        #     if count_map[0] == count_map[1] :
        #         max_contiguous_len = max(max_contiguous_len, count_map[0] + count_map[1])
        # return max_contiguous_len
        # while right < len(nums):
        #     max_contiguous_len = max(max_contiguous_len, right - left +1)
        #     if nums[right] not in count_map:
        #         count_map[nums[right]] = 1
        #     else:
        #         while left <= right and nums[left] in count_map:
        #             count_map[nums[left]] -= 1
        #             left += 1
        #     right += 1
        # return max_contiguous_len
