# https://leetcode.com/problems/split-the-array/description/

from typing import List
from collections import defaultdict

class Solution:
    # Even length list가 주어졌을 때, 이들을 distinct한 element로만 구성된
    # 2개의 동일한 길이로 나눌 수 있는지 확인
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        nums_counter = defaultdict(int)

        for num in nums:
            nums_counter[num] += 1
            if nums_counter[num] > 2:
                return False

        return True
        