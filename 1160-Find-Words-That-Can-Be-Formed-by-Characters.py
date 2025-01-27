class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        count  = 0
        freq = Counter(chars)
        for i in words:
            inside = freq.copy()
            flag = True
            for j in i :
                if inside[j] <= 0:
                    flag = False
                    break
                inside[j] -= 1
            if flag:
                count += len(i)
        return count
                
            