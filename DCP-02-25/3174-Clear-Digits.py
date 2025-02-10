class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        res = ""

        for i in range(len(s)):
            if s[i].isdigit():
                if stack:
                    stack.pop()
            else:
                stack.append(s[i])
        for i in stack:
            res += i
        return res