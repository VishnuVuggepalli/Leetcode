class Solution:
    def maxScore(self, s: str) -> int:
        max_count = zero_count = 0
        one_count = s.count('1')

        for i in range(0, len(s)-1):
            if s[i] == "1":
                one_count -= 1
            else:
                zero_count += 1
            max_count = max(max_count, zero_count + one_count)
        
        return max_count
