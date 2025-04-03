class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        R = len(board)
        C = len(board[0])
        grids = defaultdict(set)
        for i in range(R):
            rows = set()
            cols = set()
            for j in range(C):
                valRow = board[i][j]
                valCol = board[j][i]
                gridRow = i // 3
                gridCol = j // 3
                pairRow = (gridRow, gridCol)
                pairCol = (gridCol, gridRow)
                if valRow.isdigit():
                    if valRow in rows:
                        return False
                    if pairRow in grids and valRow in grids[pairRow]:
                        return False
                    rows.add(valRow)
                    grids[pairRow].add(valRow)
                if valCol.isdigit():
                    if valCol in cols:
                        return False
                    # if pairCol in grids and valCol in grids[pairCol]:
                    #     return False
                    cols.add(valCol)
                    # grids[pairCol].add(valCol)
            # print(grids)
        return True