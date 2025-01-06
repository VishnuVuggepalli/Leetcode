class Solution:
    def minOperations(self, s: str) -> List[int]:
        N = len(s)
        res = []
        suffix_counter = 0
        pref_counter = 0
        freq = 0
        for i in range(N):
            if s[i] == '1':
                pref_counter += 1
                freq += i
        print(freq)
        for j in s:
            res.append(freq)
            if j == '1':
                pref_counter -= 1
                suffix_counter += 1
            freq += suffix_counter - pref_counter
        return res