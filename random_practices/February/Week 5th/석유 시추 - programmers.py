# https://school.programmers.co.kr/learn/courses/30/lessons/250136

from typing import List

# land는 2차원 배열로, 각 칸에는 1 또는 0이 들어가 있다.
# 0이면 접근 불가능을, 1이면 접근 가능을 의미한다.
# 시추관은 해당 Land를 수직으로 온전하게 뚫고, 만나는 모든 영역을 추출 가능하다.
# 어떤 column에 시추관을 놨을 때, 해당 column에 있는 모든 점을 시발점으로 하는 영역의 합을 구하라.
# solution: BFS
# improvement: 이 때 동일 영역을 여러번 bfs하지 않도록 각각의 지점들마다 영역의 크기를 저장하고 이용하도록 한다.
def bfs(land: List[List[int]], area_id_matrix: List[List[int]], start_row: int, start_col: int, id: int) -> int:
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    queue = [(start_row, start_col)]
    area_id_matrix[start_row][start_col] = id
    area = 1

    while queue:
        current_row, current_col = queue.pop(0)
        for direction_row, direction_col in directions:
            next_row, next_col = current_row + direction_row, current_col + direction_col
            if 0 <= next_row < len(land) and 0 <= next_col < len(land[0]) and area_id_matrix[next_row][next_col] == 0 and land[next_row][next_col] == 1:
                queue.append((next_row, next_col))
                area_id_matrix[next_row][next_col] = id
                area += 1
    return area

def solution(land: List[List[int]]) -> int:
    answer = 0
    id = 1
    area_dict = {}

    area_id_matrix = [[0 for _ in range(len(land[0]))] for _ in range(len(land))]

    for row in range(len(land)):
        for col in range(len(land[0])):
            if land[row][col] == 1 and area_id_matrix[row][col] == 0:
                area = bfs(land, area_id_matrix, row, col, id)
                area_dict[id] = area
                id += 1

    for col in range(len(land[0])):
        column_sum = 0
        visited_id = set()
        for row in range(len(land)):
            if area_id_matrix[row][col] != 0 and area_id_matrix[row][col] not in visited_id:
                column_sum += area_dict[area_id_matrix[row][col]]
                visited_id.add(area_id_matrix[row][col])
        answer = max(answer, column_sum)
    return answer