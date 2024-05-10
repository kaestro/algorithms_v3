# https://leetcode.com/problems/third-maximum-number/description/

from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        if len(nums) < 3:
            return max(nums)
        
        maxes = [float('-inf'), float('-inf'), float('-inf')]
        for num in nums:
            if num > maxes[0]:
                maxes = [num, maxes[0], maxes[1]]
            elif num > maxes[1] and num < maxes[0]:
                maxes = [maxes[0], num, maxes[1]]
            elif num > maxes[2] and num < maxes[1]:
                maxes = [maxes[0], maxes[1], num]

        return maxes[-1]