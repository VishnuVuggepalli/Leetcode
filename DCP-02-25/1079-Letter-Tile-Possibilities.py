class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        alpha_count = [0] * 26
        for tile in tiles: alpha_count[ord(tile) - ord('A')] += 1

        def backtrack(alpha_count):
            res = 0
            for i in range(26):
                if not alpha_count[i] : continue
                alpha_count[i] -= 1
                res += backtrack(alpha_count) + 1
                alpha_count[i] += 1
            return res

        return backtrack(alpha_count)