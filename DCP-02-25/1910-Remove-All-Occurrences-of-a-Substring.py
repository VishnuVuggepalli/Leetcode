class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        N, M = len(s), len(part)
        if M > N:
            return s
        p = list(part)
        stack= []
        for i in range(N):
            stack.append(s[i])
            if stack[-M:] == p:
                for i in range(M):
                    stack.pop()
        
        res = ""
        for i in stack:
            res += i

        return res