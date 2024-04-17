# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/

# solution: https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/solutions/1185804/java-c-python-sort-and-one-pass/

from typing import List

class Solution:
    # 정렬한 뒤에 gap을 없앴을 때 최대 값과 동일하다.
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        prev = 0
        for num in arr:
            prev = min(prev + 1, num)
        return prev