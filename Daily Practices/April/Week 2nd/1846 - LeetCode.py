# https://leetcode.com/problems/maximum-element-after-decreasing-and-rearranging/description/

from typing import List

class Solution:
    # two rules must be satisfied after the operation:
    # 1. The first element must be 1
    # 2. The difference between the current element and the previous element must be less than or equal to 1

    # two operations can be done on each element:
    # decrease the element to any number less than or equal to the current element
    # rearrange the elements in any order

    # Return the maximum possible value of an element in arr after performing the operations to satisfy the conditions.

    # => It means that it is much more preferred to rearrange the elements compared to decreasing the elements.

    # ideal case: each elements' difference is 1 when sorted in ascending order

    # Then the problem is, the gaps between the elements are not 1, which can't be removed by rearranging the elements.

    # We also need to consider that the elements can be either increased or decreased.
    # => 짝수개의 연속한 숫자들이 짝수개의 pair로 만들어지면 삭제 가능
    
    # => gap이 있을 때는 그거 위에서 중복된 것으로 메꿔주고, 남는 것들에 대해서 생각하면 됨?
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        result = 0

        return result