# https://leetcode.com/problems/path-with-minimum-effort/description/

from typing import List
from heapq import heappop, heappush

class Solution:
    # heights is a 2D grid of integers
    # heights[row][col] is the height of the cell at row row and column col
    # starting from (0,0) and ending at (m-1, n-1), return the minimum effort it takes to travel from (0,0) to (m-1, n-1)
    # effort is defined as the absolute difference in heights
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        row_len, col_len = len(heights), len(heights[0])

        # Create a list of tuples where each tuple is (effort, row, col)
        # 해당 노드에 도착할 때 까지의 연산에 dijksra 알고리즘을 사용할 것이므로, 이를
        # 위해 우선순위 큐를 사용한다.
        effort_heap = [(0, 0, 0)]

        # Create a 2D grid of infinity
        # This will be used to keep track of the minimum effort it takes to travel to each cell
        # 최종적으로는, 각 노드에 도착할 때 까지의 최소 연산을 저장할 것이며
        # 다익스트라 알고리즘을 사용하는 중간에는 현재까지 도달한 노드에 대한 최소 연산을 저장할 것이다.
        min_efforts = [[float('inf')] * col_len for _ in range(row_len)]
        min_efforts[0][0] = 0

        # 노드가 이동할 수 있는 방향을 정의
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        # Dijkstra's algorithm
        while effort_heap:
            current_effort, current_row, current_col = heappop(effort_heap)

            if current_row == row_len - 1 and current_col == col_len - 1:
                return current_effort

            for row_diff, col_diff in directions:
                new_row, new_col = current_row + row_diff, current_col + col_diff

                if 0 <= new_row < row_len and 0 <= new_col < col_len:
                    # 문제에서 정의된 effort를 계산한다.
                    # effort는 여태까지 도달하면서 만난 노드들의 높이 차이의 최대값이다.
                    new_effort = max(current_effort, abs(heights[new_row][new_col] - heights[current_row][current_col]))

                    if new_effort < min_efforts[new_row][new_col]:
                        min_efforts[new_row][new_col] = new_effort
                        heappush(effort_heap, (new_effort, new_row, new_col))

        return -1