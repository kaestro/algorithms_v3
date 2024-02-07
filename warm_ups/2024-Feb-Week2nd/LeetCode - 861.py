# https://leetcode.com/problems/score-after-flipping-matrix/description/

from typing import List

class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        for i in range(row_len):
            if grid[i][0] == 0:
                for j in range(col_len):
                    grid[i][j] ^= 1

        flipped = True
        while flipped:
            flipped = False
            for j in range(1, col_len):
                zero_cnt = sum(grid[i][j] == 0 for i in range(row_len))
                if zero_cnt > row_len // 2:
                    flipped = True
                    for i in range(row_len):
                        grid[i][j] ^= 1
        
        # interpret the row of grid as binary number and
        # convert it to decimal number
        def to_binary_number(row):
            return sum(row[i] * (2 ** (col_len - i - 1)) for i in range(col_len))

        return sum(to_binary_number(grid[i]) for i in range(row_len))