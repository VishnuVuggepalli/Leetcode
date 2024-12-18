class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        freq = Counter(s)
        max_heap = [-ord(c) for c in freq]
        heapify(max_heap)

        ans = []
        while max_heap:
            cur_char = chr(-heappop(max_heap))
            count = min(repeatLimit, freq[cur_char])
            ans.extend([cur_char]*count)
            freq[cur_char] -= count

            if freq[cur_char] > 0:
                if not max_heap:
                    break
                
                next_char = chr(-heappop(max_heap))
                ans.append(next_char)
                freq[next_char] -= 1

                if freq[next_char] > 0:
                    heappush(max_heap, -ord(next_char))
                heappush(max_heap, -ord(cur_char))
        return ''.join(ans)


        # s = list(sorted(s, reverse =True))
        # res= ""
        # count = 0
        # left = 0
        # while left < len(s):
        #     if left > 0 and s[left-1] != s[left]:
        #         count = 0
        #     if count < repeatLimit:
        #         res += s[left]
        #         count += 1
        #         left += 1
        #     else:
        #         right = left + 1
        #         while right < len(s) and s[left] == s[right]:
        #             right += 1
        #         if right >= len(s):
        #             break
        #         res += s[right]
        #         s.pop(right)
        #         count = 0 
        # return res


