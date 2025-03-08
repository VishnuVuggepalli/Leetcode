class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        white_count = 0
        
        for i in range(k):
            if blocks[i] == 'W':
                white_count += 1
        i = 0
        min_occ = white_count
        for j in range(k,len(blocks)):
            if blocks[i] == 'W':
                white_count -= 1
            if blocks[j] == 'W':
                white_count += 1
            i+=1
            min_occ = min(min_occ, white_count)
        
        return min_occ