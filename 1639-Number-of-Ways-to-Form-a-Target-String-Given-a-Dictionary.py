# class Solution:
#     def numWays(self, words: List[str], target: str) -> int:
#         '''
#         include and skip columns
#         '''
#         MOD =  10 ** 9 + 7
#         freq = defaultdict(int)
#         # precompute
#         for word in words:
#             for i, v in enumerate(word):
#                 freq[(i,v)] += 1

#         # DP and memo
#         dp_cache ={}

#         def dp(i,k):
#             if i == len(target) : return 1
#             if k == len(words[0]) : return 0
#             if (i,k) in dp_cache : return dp_cache[(i,k)]
            
#             c = target[i]
#             # do not include
#             dp_cache[(i,k)] = dp(i,k+1)
#             # include
#             dp_cache[(i,k)] += freq[(k,c)] * dp(i+1, k+1)

#             return dp_cache[(i,k)] % MOD
#         return dp(0,0) 

class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7

        # create idx_to_counter
        word_len, target_len = len(words[0]), len(target)
        idx_to_counter = [defaultdict(int) for _ in range(word_len)]
        for w in words:
            for i in range(word_len):
                idx_to_counter[i][w[i]] += 1
        
        @cache
        def dp(i, target_i):
            if target_i == target_len: return 1
            if i == word_len: return 0

            # try skipping
            ans = dp(i + 1, target_i)
            # try adding
            desired_char = target[target_i]
            ans += idx_to_counter[i][desired_char] * dp(i + 1, target_i + 1)
            return ans % MOD
        return dp(0, 0)