# https://school.programmers.co.kr/learn/courses/30/lessons/172928

from typing import List

# routes 는 "direction distance" 형태로 주어진다.
# direction은 대문자 알파벳 WENS 중 하나이고, distance는 1 이상 9 이하의 자연수이다.
# park는 임의의 크기의 2차원 배열로, 각 원소는 "S, O, X" 중 하나이다.
# 이 때 S는 시작점, X는 장애물, O 는 빈 공간을 의미한다.
# S에서 시작해 route를 따라 이동 가능한지 확인하고, 가능할 경우 해당위치로
# 이동한다. 불가능 할 경우 해당 route로 진행하지 않고 다음 route로 넘어간다.
# 최종 위치를 반환한다.
def solution(park: List[List[str]], routes: List[str]):

    direction = {
        'W': (0, -1),
        'E': (0, 1),
        'N': (-1, 0),
        'S': (1, 0)
    }

    width, height = len(park[0]), len(park)

    current_position = None
    for i in range(height):
        for j in range(width):
            if park[i][j] == 'S':
                current_position = (i, j)
                break
        if current_position:
            break

    for route in routes:
        x, y = current_position
        dir, dist = route.split()  # split the route string by space
        dist = int(dist)  # convert the distance part to integer
        dx, dy = direction[dir]

        for _ in range(dist):
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= height or ny < 0 or ny >= width or park[nx][ny] == 'X':
                break
            x, y = nx, ny
        else:
            current_position = (x, y)

    return current_position