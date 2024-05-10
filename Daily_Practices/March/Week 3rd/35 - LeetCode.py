# https://leetcode.com/problems/search-insert-position/description/

from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_idx, right_idx = 0, len(nums) - 1
        mid_idx = left_idx + (right_idx - left_idx) // 2

        while left_idx <= right_idx:
            if nums[mid_idx] == target:
                return mid_idx
            elif nums[mid_idx] < target:
                left_idx = mid_idx + 1
            else:
                right_idx = mid_idx - 1
            mid_idx = left_idx + (right_idx - left_idx) // 2
        return left_idx