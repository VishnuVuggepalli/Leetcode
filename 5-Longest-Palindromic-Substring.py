class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 1:
            return s
        max_len = 1
        max_strs = s[0]
        dp = [[False for _ in range(len(s))] for _ in range(len(s))] 
        for i in range(len(s)):
            dp[i][i] = True
            for j in range(i):
                if s[i] == s[j] and (i -j <= 2 or dp[j+1][i-1]):
                    dp[j][i]= True
                    if i - j +1 > max_len:
                        max_len = i -j +1
                        max_strs = s[ j: i+1]

        return max_strs