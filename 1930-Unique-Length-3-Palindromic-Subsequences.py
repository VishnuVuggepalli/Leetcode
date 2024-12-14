class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        visited = []
        palindrome_count =0
        for left in range(len(s)):
            right = len(s)-1
            if s[left] not in visited:
                visited.append(s[left])
                while right > left and s[right] != s[left]:
                    right -= 1
                palindrome_count += len(set(s[left+1 : right]))
        return palindrome_count