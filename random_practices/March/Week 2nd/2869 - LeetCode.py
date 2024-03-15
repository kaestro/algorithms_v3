# https://leetcode.com/problems/minimum-operations-to-collect-elements/description/

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        target_collection = set(i for i in range(1, k + 1))

        num_idx = len(nums) - 1
        while len(target_collection) > 0:
            if nums[num_idx] in target_collection:
                target_collection.remove(nums[num_idx])
            num_idx -= 1

        return len(nums) - num_idx - 1