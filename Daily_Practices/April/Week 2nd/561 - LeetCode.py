# https://leetcode.com/problems/array-partition/description/

from typing import List

class Solution:
    # pair the integers
    # find the maximum pair list where sum(min(a, b)) is maximized

    # => min(a, b) == a - |a - b|
    # 이게 최대가 된다?는 것은, |a - b|가 최소가 되는 것이다. 즉 pair의 차이가 최소가 되는 값들을 찾아야 한다.
    def arrayPairSum(self, nums: List[int]) -> int:
        result = 0

        nums.sort()
        for i in range(0, len(nums), 2):
            result += nums[i]

        return result