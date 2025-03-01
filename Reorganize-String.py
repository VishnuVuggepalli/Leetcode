class Solution:
    def reorganizeString(self, s: str) -> str:
        # preprocess freq Count
        string_count = {}

        for i in s:
            if i in string_count:
                string_count[i] += 1
            else:
                string_count[i] = 1
        
        min_heap = [(-freq,char) for char,freq in string_count.items()]
        heapq.heapify(min_heap)
        res = []
        while min_heap:
            if len(min_heap) < 2:
                f, c = min_heap[0]
                if f < -1:
                    return "" 
            max_freq,max_char = heapq.heappop(min_heap)
            # print(max_freq,max_char )
            res.append(max_char)
            if min_heap:
                second_freq, second_char = heapq.heappop(min_heap)
                res.append(second_char)
                second_freq += 1
                if second_freq < 0:
                    heapq.heappush(min_heap, (second_freq, second_char))

            max_freq += 1
            if max_freq < 0:
                heapq.heappush(min_heap, (max_freq, max_char))
        return "".join(res)