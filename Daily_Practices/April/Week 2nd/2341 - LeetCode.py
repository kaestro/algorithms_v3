# https://leetcode.com/problems/maximum-number-of-pairs-in-array/description/

from typing import List
from collections import Counter

class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        result = [0, 0]
        nums_counter = Counter(nums)

        for count in nums_counter.values():
            result[0] += count // 2
            result[1] += count % 2

        return result