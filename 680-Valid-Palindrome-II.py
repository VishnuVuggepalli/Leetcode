class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] != s[right]:
                leave_left , leave_right = s[left+1:right+1], s[left:right]
                return (leave_left == leave_left[::-1] or leave_right == leave_right[::-1])
            left, right = left + 1, right - 1 
        return True
        # count = 0
        # while left < right:
        #     if s[left] != s[right]:
        #         count += 1
        #         if count > 1:
        #             return False
        #         if right - left > 1:
        #             if s[left + 1] != s[right] and s[right - 1] != s[left]:
        #                 return False
        #     left += 1
        #     right -= 1
        # return True