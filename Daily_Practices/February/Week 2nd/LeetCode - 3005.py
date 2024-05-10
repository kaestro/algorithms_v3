# https://leetcode.com/problems/count-elements-with-maximum-frequency/description/

from typing import List
from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        nums_cnt = Counter(nums)
        max_freq = max(nums_cnt.values())
        return sum(freq for freq in nums_cnt.values() if freq == max_freq)