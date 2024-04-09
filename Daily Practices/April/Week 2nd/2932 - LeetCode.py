# https://leetcode.com/problems/maximum-strong-pair-xor-i/description/

from typing import List

class Solution:
    # 1. Strong Pair: |x - y| <= min(x, y)
    # 2. objective: max(x ^ y) where (x, y) is a strong pair
    # Brute Force: O(n^2)
    # Question: When x ^ y gets bigger?
    # => When x and y have different bits
    # Solution: Strong Pair로 (x, y)구한 다음에, 이후에 읽은 값들 중에서
    # 더 커질 수 없으면 아예 비교하지 않음.
    # Question: 그러면 수를 아예 binary로 들고 있을까?
    # => 이건 string으로 반환돼서 안됨.
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if abs(nums[i] - nums[j]) <= min(nums[i], nums[j]):
                    result = max(result, nums[i] ^ nums[j])

        return result