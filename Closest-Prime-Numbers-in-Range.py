class Solution:
    def closestPrimes(self, l: int, r: int) -> List[int]:
        @lru_cache(None)
        def isprime(n):
            if n < 2:
                return False
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True

        p = [-1, -1]
        prev = -1
        d = {}

        for i in range(l, r + 1):
            if isprime(i):
                if prev != -1:
                    diff = i - prev
                    if diff == 1:
                        return [2, 3]
                    if diff == 2:
                        return [prev, i]
                    d[(prev, i)] = diff
                prev = i  

        return min(d, key=d.get) if d else p