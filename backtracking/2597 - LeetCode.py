# https://leetcode.com/problems/the-number-of-beautiful-subsets/description/
from typing import List, Set


class Solution:
    # set은 임의의 두 원소 간 절대값의 차이가 target_diff인 경우가 존재하지 않을
    # 경우에 beautiful하다고 한다.
    # nums의 모든 부분집합 중 beautiful한 부분집합의 개수를 반환하라.

    # 1. backtracking을 통해서 모든 부분집합을 구한다.
    # 2. 각 부분집합에 대해서 target_diff인 경우가 존재하는지 확인한다.
    # 이 때 target_diff인 경우를 순회를 통해서 찾을 경우 O(n^2)의 시간복잡도가
    # 발생한다.
    # 그렇다면 일반적으로 backtracking을 통해서 집합해서 빼내던 것과 반대로,
    # backtrack을 통해 새로운 set을 만들어나가는 방식으로 해결할 수 있을 것이다.
    # 이 때 저장하는 자료구조는 list가 아닌 set을 사용하면 순회가 아니라 O(1)의
    # 시간복잡도로 찾을 수 있다.

    # BackTrack의 순회 자체의 시간복잡도는 O(2^n)이다. => 감당 가능?
    def beautifulSubsets(self, nums: List[int], target_diff: int) -> int:
        countedSubsets = []
        def backTrack(nums: List[int], idx: int, subset: Set[int], target_diff: int) -> int:
            if idx == len(nums):
                # 주의: list내에서 set은 in으로 찾을 수 없다.
                if len(subset) == 0 or str(subset) in countedSubsets:
                    return 0
                else:
                    countedSubsets.append(str(subset))
                    return 1

            cnt = backTrack(nums, idx + 1, subset.copy(), target_diff)
            if nums[idx] - target_diff not in subset and nums[idx] + target_diff not in subset:
                subset.add(nums[idx])
                cnt += backTrack(nums, idx + 1, subset, target_diff)
            return cnt
        
        return backTrack(nums, 0, set(), target_diff)