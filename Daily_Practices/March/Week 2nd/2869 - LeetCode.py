# https://leetcode.com/problems/minimum-operations-to-collect-elements/description/

from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        target_collection = set(i for i in range(1, k + 1))

        num_idx = len(nums) - 1
        while len(target_collection) > 0:
            target_collection.discard(nums[num_idx])
            num_idx -= 1

        return len(nums) - num_idx - 1
    
    def better_minOperations(self, nums: List[int], k: int) -> int:
        occurrenceSet = set()
        minOperations = 0

        for num in reversed(nums):
            if num <= k:
                occurrenceSet.add(num)
            
            minOperations += 1

            if len(occurrenceSet) == k:
                break
        
        return minOperations