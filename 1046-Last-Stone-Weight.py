class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''maxcnt =0
        if nums.count(0) <= k:
            return len(nums)
        for l in range(len(nums)):
            cnt =0
            if nums[l] == 0:
                cnt += 1 
            r = l+1
            while cnt <= k and r < len(nums) :
                if cnt <= k: 
                    print(nums[l:r], l, r)
                    maxcnt = max(maxcnt, r-l)
                if nums[r] == 0:
                    cnt +=1
                    r+=1
                else:
                    r+=1
            
        return maxcnt'''
        l =0
        for r in range(len(nums)):
            if nums[r] ==0 :
                k -=1
            if k < 0:
                if nums[l] == 0:
                    k+=1
                l+=1
        return r-l+1

        