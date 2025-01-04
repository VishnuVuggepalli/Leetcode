class Solution:
    def partitionString(self, s: str) -> int:
        seen = set()
        cnt = 1
        for i in s:
            if i not in seen:
                seen.add(i)
            else:
                seen = {i}
                cnt += 1
        print(seen)
        return cnt
                