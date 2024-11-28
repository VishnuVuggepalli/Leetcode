class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # condition 1  - n : no on open's and close's =  n
        # condition 2 - we must always start with an open paranthesis
        # condition 3 - if open < n add opens
        # condition 4 - if closes less than open add closes and cela up as you go 
        stack =[]
        res =[]
        def backTrack(openBracket, closedBracket):
            if openBracket == closedBracket == n:
                res.append(\\.join(stack))
                return 
            if openBracket < n:
                stack.append(\(\)
                backTrack(openBracket+1,closedBracket)
                stack.pop()
            if closedBracket < openBracket:
                stack.append(\)\)
                backTrack(openBracket, closedBracket+1)
                stack.pop()
        backTrack(0,0)
        return res
