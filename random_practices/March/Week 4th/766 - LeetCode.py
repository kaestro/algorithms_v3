# https://leetcode.com/problems/toeplitz-matrix/description/

from typing import List

class Solution:
    # Toepliz Matrix는 대각선 방향으로 같은 숫자가 있는지 확인한 matrix를 말한다.

    # Brute Force
    # 대각선 방향으로 element를 확인한다.
    # 문제점: List는 row 단위로 접근하기 때문에, 대각선 방향 접근은 효율적이지 못하다.
    # 해결방법: (i, j)를 key로 쓰는 dictionary를 통해 확인한다.
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:

        matrix_dict = {(i, j) : matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0]))}
        is_toeplitz = True


        for i in range(len(matrix)):
            default_value = matrix_dict[(i, 0)]
            row_idx, col_idx = i, 0
            while (row_idx, col_idx) in matrix_dict:
                if matrix_dict[(row_idx, col_idx)] != default_value:
                    is_toeplitz = False
                    break
                row_idx, col_idx = row_idx + 1, col_idx + 1
        
        for j in range(1, len(matrix[0])):
            default_value = matrix_dict[(0, j)]
            row_idx, col_idx = 0, j
            while (row_idx, col_idx) in matrix_dict:
                if matrix_dict[(row_idx, col_idx)] != default_value:
                    is_toeplitz = False
                    break
                row_idx, col_idx = row_idx + 1, col_idx + 1

        return is_toeplitz