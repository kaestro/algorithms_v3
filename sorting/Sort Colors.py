# https://leetcode.com/explore/learn/card/sorting/694/comparison-based-sorts/4483/
# implementation of selection sort

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
            minIdx = i
            for j in range(i, len(nums)):
                if nums[minIdx] > nums[j]:
                    minIdx = j
            nums[i], nums[minIdx] = nums[minIdx], nums[i]


if __name__ == "__main__":
    nums = [2,0,4,2,1,1,0]
    test = Solution()
    test.sortColors(nums)
    print(nums)