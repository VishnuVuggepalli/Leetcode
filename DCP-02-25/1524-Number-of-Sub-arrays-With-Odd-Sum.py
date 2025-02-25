class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []
        N = len(words)
        for i in range(N):
            for j in range(N):
                if i!= j and words[j].find(words[i]) != -1:
                    res.append(words[i])
                    break
        
        return res