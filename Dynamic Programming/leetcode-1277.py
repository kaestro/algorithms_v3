# https://leetcode.com/problems/count-square-submatrices-with-all-ones/description/

from typing import List


class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        row_len, col_len = len(matrix), len(matrix[0])
        dp = [[0] * col_len for _ in range(row_len)]

        for i in range(col_len):
            dp[0][i] = matrix[0][i]
        
        for j in range(row_len):
            dp[j][0] = matrix[j][0]
        
        for i in range(1, row_len):
            for j in range(1, col_len):
                if matrix[i][j] == 0:
                    continue

                dp[i][j] = min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1]) + 1

        return sum(map(sum, dp))


if __name__ == "__main__":
    matrix = [
                [1,0,1],
                [1,1,0],
                [1,1,0] ]
    
    print(Solution().countSquares(matrix))