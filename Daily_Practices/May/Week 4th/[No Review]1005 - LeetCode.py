# https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:

        heapify(nums)
        while k > 0:
            head = heappop(nums)
            if head < 0:
                head = -head
                heappush(nums, head)
            else:
                heappush(nums, head)
                break
            k -= 1

        if (k % 2) == 1:
            head = heappop(nums)
            head = -head
            nums.append(head)

        return sum(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.largestSumAfterKNegations([4, 2, 3], 1))  # 5
