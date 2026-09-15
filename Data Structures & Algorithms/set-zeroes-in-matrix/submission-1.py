class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = {}
        cols = {}

        for row in range(0,len(matrix)):
            for col in range(0,len(matrix[0])):
                if matrix[row][col] == 0:
                    if row not in rows:
                        rows[row] = True
                    if col not in cols:
                        cols[col] = True
        
        for row in rows:
            matrix[row] = [0] * len(matrix[0])
        
        for col in cols:
            for i in range(len(matrix)):
                matrix[i][col] = 0

        