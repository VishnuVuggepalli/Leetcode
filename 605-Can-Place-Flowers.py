class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0 : return True
        N = len(flowerbed)
        if N == 1:
            return True if flowerbed[0] == 0 else False
        for i in range(N):
            if flowerbed[i] == 0:
                if (i-1 < 0 and flowerbed[i+1] == 0) or (i+1 == N and flowerbed[i-1] == 0):
                    n -= 1
                    flowerbed[i] = 1
                elif flowerbed [i-1] == 0 and flowerbed[i+1] == 0:
                    n -= 1
                    flowerbed[i] = 1
                if n == 0: return True
        return n == 0
                