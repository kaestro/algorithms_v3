# https://leetcode.com/problems/sum-of-all-subset-xor-totals/description/

from typing import List

class Solution:
    # get the total sum of subsetXOR values
    def subsetXORSum(self, nums: List[int]) -> int:

        def backTrack(idx: int, subset:List[int], subsets: List[List[int]]):
            if idx == len(nums):
                subsets.append(subset)
                return
            
            backTrack(idx + 1, subset + [nums[idx]], subsets)
            backTrack(idx + 1, subset, subsets)
        
        subsets = []
        backTrack(0, [], subsets)

        sum = 0
        for _, subset in enumerate(subsets):
            xorSum = 0
            for num in subset:
                xorSum ^= num
            sum += xorSum

        return sum


if __name__ == "__main__":
    nums = [1, 3]

    print(Solution().subsetXORSum(nums))