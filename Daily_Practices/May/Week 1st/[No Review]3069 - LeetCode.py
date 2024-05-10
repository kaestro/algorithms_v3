# https://leetcode.com/problems/distribute-elements-into-two-arrays-i/

from typing import List

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        arrLeft, arrRight = [nums[0]], [nums[1]]
        idx = 2
        while idx < len(nums):
            if arrLeft[-1] > arrRight[-1]:
                arrLeft.append(nums[idx])
            else:
                arrRight.append(nums[idx])
            idx += 1
        return arrLeft + arrRight

        