# https://leetcode.com/problems/count-negative-numbers-in-a-sorted-matrix/description/
from typing import List

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for num in row[::-1]:
                if num < 0:
                    count += 1
                else:
                    break
        return count