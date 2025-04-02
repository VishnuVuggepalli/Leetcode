class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        no ordering

        A hashmap , to keep track of freq ; form map with magazine and delete vals with ransomNote, if negative , return false, else True
        '''

        alpha_freq = [0] *26

        for ch in magazine:
            alpha_freq[ord(ch) - ord(\a\)] += 1
        
        for ch in ransomNote:
            idx = ord(ch) - ord(\a\)
            if alpha_freq[idx] <= 0 : return False
            alpha_freq[idx] -= 1
        return True