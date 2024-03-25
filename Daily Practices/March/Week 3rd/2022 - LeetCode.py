# https://leetcode.com/problems/convert-1d-array-into-2d-array/description/

from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n:
            return []
        
        result = []
        for i in range(0, len(original), n):
            result.append(original[i:i + n])

        return result