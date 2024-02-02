# https://leetcode.com/problems/rank-transform-of-an-array/description/

from typing import List

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorted_arr = sorted(set(arr))
        rank_dict = {}
        for rank, num in enumerate(sorted_arr, 1):
            rank_dict[num] = rank
        return [rank_dict[num] for num in arr]


if __name__ == "__main__":
    input = [37, 12, 28, 9, 100, 56, 80, 5, 12]
    input = [40, 10, 20, 30]
    Solution().arrayRankTransform(input)