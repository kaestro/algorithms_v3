# https://school.programmers.co.kr/learn/courses/30/lessons/181188

from typing import List

# targets의 원소는 (a, b)로 a에서 시작해서 b로 끝나는 구간을 의미한다.
# 이 때 a, b는 포함하지 않는다.
# targets의 원소를 모두 관통하는 최소 개수를 구하라.
# 여기서 관통한다는 것은 a < x < b를 만족하는 x가 존재한다는 것을 의미한다.
# 예를 들어, targets = [[1, 3], [2, 4], [3, 5]]라면 2, 3, 4를 포함하는 구간이 존재하므로 3개를 반환한다.
def solution(targets:List[List[int]])->int:
    answer = 0

    targets = [[x[0] + 1, x[1] - 1] for x in targets]

    # targets를 먼저 시작점으로, 그 후에 끝점으로 정렬한다.
    targets = sorted(targets, key=lambda x: x[1])

    # 현재까지의 최대 끝점을 저장한다.
    last_end = -1

    for start, end in targets:
        # 현재 구간의 시작점이 이전 구간의 끝점보다 크거나 같은 경우
        if start > last_end:
            # 이전 구간의 끝점을 현재 구간의 끝점으로 갱신하고, 구간의 개수를 1 증가시킨다.
            last_end = end
            answer += 1

    return answer