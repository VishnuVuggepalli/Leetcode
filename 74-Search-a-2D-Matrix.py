class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # def binary_search(row, col):
        row = len(matrix)
        col = len(matrix[0])
        row_num , col_num = 0, (row*col) -1

        while row_num <= col_num:
            mid = (row_num + col_num)//2

            if target == matrix[mid//col][mid% col]:
                return True
            elif target < matrix[mid//col][mid% col]:
                col_num = mid -1
            else:
                row_num = mid + 1
        return False