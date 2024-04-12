# https://leetcode.com/problems/find-the-highest-altitude/description/

from typing import List

class Solution:

    # 1. Start at 0
    # 2. 매번 진행하는 과정 중 가장 높은 고도를 반환하라

    # Bruteforce
    # Simple iteration: O(n)
    def largestAltitude(self, gains: List[int]) -> int:
        highest = 0

        current = 0
        for gain in gains:
            current += gain
            if current > highest:
                highest = current

        return highest