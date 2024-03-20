# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/

from typing import List

class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = set()
        for idx, num in enumerate(nums):
            if num == key:
                result.update(idx for idx in range(max(0, idx - k), min(idx + k + 1, len(nums))))
        return sorted(result)