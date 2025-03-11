class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        word_count = defaultdict(int)
        sub_strs = 0
        i,j = 0,0
        while j < len(s):
            word_count[s[j]] += 1
            while len(word_count) == 3:
                sub_strs += len(s) - j
                if s[i] in word_count:
                    word_count[s[i]] -= 1
                    if word_count[s[i]] == 0:
                        del word_count[s[i]]
                i += 1
            j += 1

        return sub_strs