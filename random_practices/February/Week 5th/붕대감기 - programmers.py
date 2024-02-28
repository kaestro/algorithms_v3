# https://school.programmers.co.kr/learn/courses/30/lessons/250137

from typing import List

# bandage는 [시전 시간, 초당 회복량, 추가 회복량]으로 이루어진 배열
# 시전 시간 동안 초당 회복량에 맞춰 회복하고, 시전 시간을 채울 경우 추가 회복이 발생한다.

# health는 최대 체력

# attacks는 [[공격 시간, 피해량]]으로 공격 시간을 기준으로 오름차순 정렬돼있다.

# 공격이 끝난 뒤 살아남으면 남은 체력을, 죽으면 -1을 반환한다.
def solution(bandage: List[int], max_health: int, attacks: List[List[int]]) -> int:
    current_health = max_health
    heal_duration, heal_per_sec, additional_heal = bandage
    end_time = attacks[-1][0]
    current_heal_time = 0

    for current_time in range(end_time + 1):
        # 공격을 받을 시간이면 체력을 깎는다. 힐은 하지 않는다.
        if attacks and current_time == attacks[0][0]:
            current_health -= attacks[0][1]

            if current_health <= 0:
                return -1

            current_heal_time = 0
            attacks.pop(0)
            continue

        current_health += heal_per_sec
        current_heal_time += 1

        # 회복을 받을 시간이면 체력을 회복한다.
        if current_heal_time % heal_duration == 0:
            current_health += additional_heal

        current_health = min(current_health, max_health)




    return current_health