class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        
        res =[]
        pref = []
        vowels = ("a","e","i","o","u")
        cnt  = 0
        for cnr in words:
            if cnr[0] in vowels and cnr[-1] in vowels:
                cnt += 1
            pref.append(cnt)
        for i,j in queries:
            if i > 0 :
                diff = pref[j] - pref[i-1]
            else:
                diff = pref[j] - 0
            res.append(diff)
        return res