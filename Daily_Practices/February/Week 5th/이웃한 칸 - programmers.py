# https://school.programmers.co.kr/learn/courses/30/lessons/250125

from typing import List

# board는 2차원 배열로, 영어 소문자로 된 색을 표현하는 문자열이다.
# (row_idx, col_idx)를 기준으로 이웃한 칸들 중 같은 색으로 칠해져 있는 칸의 개수를 return하도록 구현하라.
def solution(board: List[List[str]], row_idx: int, col_idx: int) -> int:
    answer = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    original_color = board[row_idx][col_idx]

    for direction in directions:
        new_row, new_col = row_idx + direction[0], col_idx + direction[1]

        if 0 <= new_row < len(board) and 0 <= new_col < len(board[0]) and board[new_row][new_col] == original_color:
            answer += 1
    return answer