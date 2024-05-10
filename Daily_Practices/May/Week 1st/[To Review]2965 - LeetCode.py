# https://leetcode.com/problems/find-missing-and-repeated-values/description/

from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        gridLen = len(grid) * len(grid[0])
        expectedSum = gridLen * (gridLen + 1) // 2
        expectedSumSquare = gridLen * (gridLen + 1) * (2 * gridLen + 1) // 6
        actualSum = sum(cell for row in grid for cell in row)
        actualSumSquare = sum(cell ** 2 for row in grid for cell in row)
        
        repeatedMinusMissing = expectedSum - actualSum
        repeatedMinusMissingSquared = expectedSumSquare - actualSumSquare
        
        missing = (repeatedMinusMissingSquared // repeatedMinusMissing + repeatedMinusMissing) // 2
        repeating = (repeatedMinusMissingSquared // repeatedMinusMissing - repeatedMinusMissing) // 2
        
        return [repeating, missing]