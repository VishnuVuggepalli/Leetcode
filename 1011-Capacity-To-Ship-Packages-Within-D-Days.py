class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        min_w = max(weights)
        max_w = sum(weights)
        res = max_w

        def can_ship(cap):
            ships = 1
            new_w = cap
            for w in weights:
                if new_w - w < 0:
                    ships += 1
                    new_w = cap
                new_w -= w
            return ships <= days        

        while min_w <= max_w:
            cap = (min_w + max_w) // 2
            if can_ship(cap):
                res = min(cap,res)
                max_w = cap-1
            else:
                min_w = cap+1
        return res