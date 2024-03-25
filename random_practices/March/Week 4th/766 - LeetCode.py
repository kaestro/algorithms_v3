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
    
    # matrix의 모든 값을 저장하지 않고, 맨 처음 row와 column의 값을 저장한다.
    # list를 순회하면서 첫 row와 column의 값과 비교한다.
    # memory 사용량 0.4MB 감소 => 매트릭스의 크기가 커질수록 차이가 더 커질 것으로 예상된다.
    # [improve tip] key로 (i, j)가 아니라 (i - j)를 사용하는 방법도 있다.
    def improvedIsToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        matrix_dict = {(i, j) : matrix[i][j] for i in range(len(matrix)) for j in range(len(matrix[0])) if i == 0 or j == 0}

        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[0])):
                row_idx, col_idx = i - min(i, j), j - min(i, j)
                if matrix_dict[(row_idx, col_idx)] != matrix[i][j]:
                    return False
        
        return True