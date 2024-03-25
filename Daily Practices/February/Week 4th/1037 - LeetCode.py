# https://leetcode.com/problems/valid-boomerang/description/

from typing import List

class Solution:
    # boomerang is a set of 3 points that are not in a straight line
    def isBoomerang(self, points: List[List[int]]) -> bool:
        if points[0] == points[1] or points[1] == points[2] or points[0] == points[2]:
            return False

        inclination_1 = (points[1][1] - points[0][1]) / (points[1][0] - points[0][0]) if points[1][0] - points[0][0] != 0 else float('inf')
        inclination_2 = (points[2][1] - points[0][1]) / (points[2][0] - points[0][0]) if points[2][0] - points[0][0] != 0 else float('inf')

        return inclination_1 != inclination_2
