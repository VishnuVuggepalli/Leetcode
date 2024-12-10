class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()
        prefix = strs[0]

        for word in range(1, len(strs)):
            while prefix != strs[word][:len(prefix)]:
                prefix = prefix[:-1]
                if prefix== \\:
                    return \\
        return prefix

            
