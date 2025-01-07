class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N, M = len(str1), len(str2)

        def is_divisor(div):
            if N % div or M % div:
                return False
            f1, f2 = N // div, M // div
            return str1[:div] * f1 == str1 and str1[:div] * f2 == str2

        for i in range(min(N,M), 0, -1):
            if is_divisor(i):
                return str1[:i]
        return ""