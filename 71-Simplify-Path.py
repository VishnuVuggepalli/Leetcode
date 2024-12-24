class Solution:
    def simplifyPath(self, path: str) -> str:
        files = path.split(\/\)
        stack= []
        print(files)
        for path_var in files:
            if stack and path_var == \..\:
                stack.pop()
            elif path_var not in [\\,\.\, \..\]:
                stack.append(path_var)
        return \/\+\/\.join(stack)