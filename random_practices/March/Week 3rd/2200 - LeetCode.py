# https://leetcode.com/problems/find-all-k-distant-indices-in-an-array/description/

from typing import List

class Solution:
    # key에 해당하는 값을 찾아서 k만큼 떨어진 인덱스를 찾는 문제
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        result = set()
        for idx, num in enumerate(nums):
            if num == key:
                result.update(idx for idx in range(max(0, idx - k), min(idx + k + 1, len(nums))))
        return sorted(result)
    
    from typing import List

    # sliding window를 통해 문제를 해결하는 방법
    def slidingWindowFindKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        window_start_idx = 0
        result = set()

        for key_position in range(len(nums)):
            if nums[key_position] == key:
                while window_start_idx <= k + key_position:
                    if abs(key_position - window_start_idx) <= k and window_start_idx < len(nums):
                        result.add(window_start_idx)
                    window_start_idx += 1
                
        return sorted(result)