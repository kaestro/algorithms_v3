# https://leetcode.com/problems/semi-ordered-permutation/description/

from typing import List

class Solution:
    def semiOrderedPermutation(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = nums.index(1), nums.index(n)
        return i + n - 1 - j - (i > j)