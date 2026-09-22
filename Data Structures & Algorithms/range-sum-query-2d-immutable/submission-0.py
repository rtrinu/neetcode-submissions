class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        num_cols = len(matrix[0])
        num_rows = len(matrix)
        self.sum_matrix = [[0] * (num_cols + 1) for r in range(num_rows +1)]
        for r in range(num_rows):
            prefix=0
            for c in range(num_cols):
                prefix+=matrix[r][c]
                self.sum_matrix[r+1][c+1] = prefix + self.sum_matrix[r][c+1]
            
    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        r1,c1,r2,c2 = row1+1, col1+1, row2+1, col2+1
        bottom_right = self.sum_matrix[r2][c2]
        above = self.sum_matrix[r1-1][c2]
        left = self.sum_matrix[r2][c1-1]
        top_left = self.sum_matrix[r1-1][c1-1]
        return bottom_right - above -left +top_left


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)