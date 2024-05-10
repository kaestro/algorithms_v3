# https://leetcode.com/problems/count-the-number-of-incremovable-subarrays-i/description/

from typing import List

class Solution:
    # incremovableSubarray는 주어진 배열에서 제거했을 때, 기존의 배열이
    # 증가하는 순서가 되도록 하는 subarray를 의미한다.
    # 주어진 배열에서 incremovableSubarray의 개수를 반환하는 문제이다.

    # Brute Force
    # 모든 subarray를 구한다. => O(n^2)
    # 해당 subarray를 제거한다. => O(n)
    # => O(n^3): subarray 별로 제거하는 과정을 반복한다.
    # 제거한 이후의 배열이 증가하는 순서인지 확인한다. => O(n)

    # => 개선하려면 모든 subarray를 구하는 과정을 개선해야 한다.
    # => 아니면 subarray 구한 순간에 증가하는 순서인지 확인하면?

    # 예를 들어 isIncremovableSubarray(i, j)를 구현한다 하면 이 때
    # isIncremovableSubarray(i, j) = isIncreasing(0, i) and isIncreasing(j, n) 이 된다.
    # 그러면 dp로 isIncreasing을 구해두면 될듯?
    def incremovableSubarrayCount(self, nums: List[int]) -> int:
        isIncreasingSubarray = {(0, -1): True, (len(nums), len(nums) - 1): True}        
        result = 0

        for i in range(len(nums)):
            for j in range(i, len(nums)):
                isIncreasingSubarray[(i, j)] = self.isIncreasing(nums, i, j)
        
        for i in range(len(nums)):
            for j in range(i, len(nums)):
                if isIncreasingSubarray.get((0, i - 1), True) and isIncreasingSubarray.get((j + 1, len(nums) - 1), True):
                    if nums[j+1] > nums[i-1] if i > 0 and j < len(nums) - 1 else True:
                        result += 1

        return result
    
    # [start, end] 사이의 subarray가 증가하는 순서인지 확인한다.
    def isIncreasing(self, nums: List[int], start: int, end: int) -> bool:
        for i in range(start, end):
            if nums[i] >= nums[i+1]:
                return False
        return True
    

if __name__ == "__main__":
    Solution().incremovableSubarrayCount([8, 7, 6, 6])