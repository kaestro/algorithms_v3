# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        min_num = nums[0]
        max_diff = -1
        for num in nums[1:]:
            if num > min_num:
                max_diff = max(max_diff, num - min_num)
            else:
                min_num = num
        return max_diff


if __name__ == "__main__":
    print(Solution().maximumDifference([9,4,3,2]))