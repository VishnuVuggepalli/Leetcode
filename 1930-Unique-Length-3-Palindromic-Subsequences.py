class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        alpha_set = set()
        palin_count =0
        for i in range(len(s)):
            j = len(s) - 1
            if s[i] not in alpha_set:
                alpha_set.add(s[i])
                while s[j] != s[i]:
                    j -= 1
                palin_count += len(set(s[i+1:j]))
        
        return palin_count
            