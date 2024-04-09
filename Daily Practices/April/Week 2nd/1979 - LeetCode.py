# https://leetcode.com/problems/find-greatest-common-divisor-of-array/description/

from typing import List

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_num, max_num = min(nums), max(nums)

        result = self.utilGCD(min_num, max_num)

        return result
    
    def utilGCD(self, left: int, right: int) -> int:

        while right:
            left, right = right, left % right

        return left