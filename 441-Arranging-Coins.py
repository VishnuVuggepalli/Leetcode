class Solution:
    def arrangeCoins(self, n: int) -> int:
        low , high =0 , n
        while low <= high:
            mid = low + (high - low) // 2
            k = mid*(mid +1) // 2 #check if mid gives triangular number
            if k == n:
                return mid
            elif k < n :
                low = mid + 1
            else:
                high = mid - 1
        return high