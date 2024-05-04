# https://leetcode.com/problems/maximum-difference-between-increasing-elements/description/
from typing import List

class Solution:
    def maximumDifference(self, nums: List[int]) -> int:
        sorted_nums_with_idx = sorted(((num, idx) for idx, num in enumerate(nums)), reverse=True)
        maxDiff = float('-inf')
        for curr_idx, curr_num in enumerate(nums[:-1]):
            max_idx = sorted_nums_with_idx[0][1]
            while max_idx <= curr_idx:
                for _, s_idx in sorted_nums_with_idx:
                    if s_idx > curr_idx:
                        max_idx = s_idx
                        break

            if curr_idx != max_idx:
                maxDiff = max(maxDiff, nums[max_idx] - curr_num)

        return maxDiff if maxDiff != float('-inf') else -1


if __name__ == "__main__":
    print(Solution().maximumDifference([9,4,3,2]))