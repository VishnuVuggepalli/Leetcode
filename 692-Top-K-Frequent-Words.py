class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # pre processing
        freq = defaultdict()
        for word in words:
            if word not in freq:
                freq[word] = 0
            freq[word] += 1
        
        min_heap = []
        for w,f in freq.items():
            min_heap.append([-1 * f,w])
        heapq.heapify(min_heap)

        freq_words = []

        while min_heap:
            if k == 0:
                break
            f,w = heapq.heappop(min_heap)
            freq_words.append(w)
            k -= 1
        
        return freq_words