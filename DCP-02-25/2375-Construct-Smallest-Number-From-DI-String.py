class Solution:
    def smallestNumber(self, pattern: str) -> str:
        N = len(pattern)
        smallest = ""
        stack = []

        for i in range(N+1):
            stack.append(i+1)

            if i == N or pattern[i] == "I":
                while stack:
                    smallest += str(stack.pop())
        return smallest