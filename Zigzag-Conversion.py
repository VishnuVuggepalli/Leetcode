class Solution:
    def convert(self, s: str, numRows: int) -> str:
        '''
        can the rows be 1 or greater or a greater then len(s)
        if numRows = 2 : so alternating is printed
        p + numRows-1 +numRows -2
        '''
        if numRows == 1:
            return s

        res = [\\] * numRows
        counter = False
        row = 1

        for i in range(len(s)):
            res[row -1] += s[i]
            if row == numRows:
                counter = True
            elif row == 1:
                counter = False
            
            if counter:
                row -= 1
            else:
                row += 1
        
        return \\.join(res)