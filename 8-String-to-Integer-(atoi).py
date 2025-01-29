class Solution:
    def myAtoi(self, s: str) -> int:
        '''
        Input Conditions:
        1. start can be +/-
        2. start - end both must be natural numbers 
        3. remove all leading 0 , but count all trailing 0
        '''
        strInt:str = \\
        sign = 1
        i =0
        while i < len(s) and s[i] == ' ':
            i += 1
        if i < len(s) and s[i] in ('+', '-'):
            sign = -1 if s[i] == '-' else +1
            i += 1
        while i < len(s) and s[i].isdigit():
            strInt += s[i]
            i += 1
        return max( -2 ** 31, min(sign * int(strInt or 0) , 2 ** 31 -1))
        