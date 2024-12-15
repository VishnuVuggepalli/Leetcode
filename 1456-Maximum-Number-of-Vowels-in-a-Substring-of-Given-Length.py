class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        right = 0
        vowels = {"a","e","i","o","u"}
        count = max_count = 0
        for right in range(k):
            if s[right] in vowels:
                count += 1
        max_count = count
        for right in range(k , len(s)):
            if s[right - k] in vowels:
                count -= 1
            if s[right] in vowels:
                count += 1
            max_count = max(count, max_count)
        return max_count 

