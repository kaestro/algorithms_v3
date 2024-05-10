# https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/description/

from typing import List

class Solution:
    # water_capacity는 3가지 다른 종류의 물의 양을 의미한다.
    # 매번 컵으로 물을 따라서 모든 water_capacity를 채우는데 걸리는 최소 시간을 반환하라.
    # 컵은 매번 하나의 물을 채우거나, 두 개의 다른 물을 1씩 채울 수 있다.

    # 가장 많은 물을 담을 수 있는 컵을 먼저 채우는 것이 최선이다.
    # 그러다가 그 컵이 다른 컵의 물과 채워야하는 물의 양이 같아지면,
    # 그 다음으로 가장 많은 물을 담을 수 있는 컵을 채우는 것이 최선이다.
    # 위 과정을 반복한다.
    def fillCups(self, water_capacities: List[int]) -> int:

        water_capacities.sort(reverse=True)
        max_time = 0

        while water_capacities[0] > 0:
            max_time += 1

            water_capacities[0] -= 1
            if water_capacities[1] > 0:
                water_capacities[1] -= 1
            
            water_capacities.sort(reverse=True)

        return max_time