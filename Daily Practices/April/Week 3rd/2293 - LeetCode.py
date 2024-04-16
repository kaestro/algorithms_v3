# https://leetcode.com/problems/min-max-game/description/

from typing import List

class Solution:
    # 1. if len(nums) == 1, end the process. Otherwise, create integer array with the length of len(nums) // 2
    # 2. for index where i % 2 == 0 && 0 <= i < len(nums) // 2, nums[i] = max(nums[2 * i], nums[2 * i + 1])
    # 3. for index where i % 2 == 1 && 0 <= i < len(nums) // 2, nums[i] = min(nums[2 * i], nums[2 * i + 1])
    def minMaxGame(self, nums: List[int]) -> int:
        result = 0
        numLen = len(nums)
        while numLen > 1:
            numLen //= 2
            for i in range(numLen):
                if i % 2 == 0:
                    nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    nums[i] = max(nums[2 * i], nums[2 * i + 1])

        return nums[0]