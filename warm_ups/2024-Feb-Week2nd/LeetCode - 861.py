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


    # 1. 실제로 수를 다 만든 다음에 더할 필요가 없다는 사실에 유의해야 한다.
    # 2. 맨 앞의 열은 이미 1이므로 그냥 row의 갯수에 2^(col_len - 1)을 곱해주면 된다.
    # 3. 그 다음 열부터는 0의 갯수와 1의 갯수를 비교해서 더 큰 것을 선택한 뒤, 열의
    #   위치에 따라 2의 거듭제곱을 곱해주면 된다.
    def better_matrixScore(self, grid: List[List[int]]) -> int:
        row_len = len(grid)
        col_len = len(grid[0])
        for i in range(row_len):
            if grid[i][0] == 0:
                for j in range(col_len):
                    grid[i][j] ^= 1

        res = (1 << (col_len - 1)) * row_len
        for j in range(1, col_len):
            one_cnt = sum(grid[i][j] == 1 for i in range(row_len))
            res += max(one_cnt, row_len - one_cnt) * (1 << (col_len - j - 1))
        return res
