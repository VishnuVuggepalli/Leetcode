class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        N, M = len(word1), len(word2)
        res = ""
        p = min(N,M)
        for i in range(p):
            res += word1[i]
            res += word2[i]
        
        if N-p >= 1:
            res += word1[p:]
        if M-p >= 1:
            res += word2[p:]
        
        return res