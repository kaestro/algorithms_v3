# https://leetcode.com/problems/projection-area-of-3d-shapes/description/

from typing import List

class Solution:

    # gridHeights는 (i, j) 위치의 높이를 나타낸다.
    # 이 때 각각의 xy, yz, zx 평면에 대한 투영면적의 합을 구하라.
    # xy 평면에 대한 투영 면적은 gridHeights의 각 원소가 0보다 큰 경우의 수와 같다.
    # 이런 새로운 List를 만들어내는 방법을 나머지 두 평면에 대해서도 적용할 수 있을까?
    def projectionArea(self, gridHeights: List[List[int]]) -> int:
        result = self.zxArea(gridHeights) + self.xyArea(gridHeights) + self.yzArea(gridHeights)
        return result
    
    def xyArea(self, gridHeights: List[List[int]]) -> int:
        result = sum([1 for row in gridHeights for height in row if height > 0])
        return result
    
    def yzArea(self, gridHeights: List[List[int]]) -> int:
        result = sum(max(row) for row in gridHeights)
        return result
    
    def zxArea(self, gridHeights: List[List[int]]) -> int:
        result = sum(max(column) for column in zip(*gridHeights))
        return result