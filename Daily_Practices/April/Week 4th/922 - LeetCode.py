# https://leetcode.com/problems/sort-array-by-parity-ii/description/

from typing import List

class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        result: List[int] = [0] * len(nums)
        oddIdx, evenIdx = 1, 0
        for num in nums:
            if num % 2 == 0:
                result[evenIdx] = num
                evenIdx += 2
            else:
                result[oddIdx] = num
                oddIdx += 2

        return result
        