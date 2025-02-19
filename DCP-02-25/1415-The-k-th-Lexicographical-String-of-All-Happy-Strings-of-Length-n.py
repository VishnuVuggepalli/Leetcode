class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        
        def dfs(cur_str):
            if len(cur_str) == n:
                happy_strings.append(cur_str)
                return
            
            for i in "abc":
                if cur_str and cur_str[-1] == i:
                    continue
                dfs(cur_str + i)
        
        happy_strings = []
        dfs("")

        return "" if len(happy_strings) < k else happy_strings[k-1]