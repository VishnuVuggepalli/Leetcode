class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        triangle = []

        if numRows >= 1:
            triangle.append([1])
        if numRows >= 2:
            triangle.append([1,1])
        
        for i in range(2,numRows):
            row = [1]
            for j in range(1,i):
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
            row.append(1)
            triangle.append(row)
        
        return triangle
            