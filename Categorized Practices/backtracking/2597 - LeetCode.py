# https://leetcode.com/problems/the-number-of-beautiful-subsets/description/
from typing import List
from collections import defaultdict, Counter


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

    # 궁금한점 => subset을 copy하는 것 자체가 문제 아닐까? copy하지 않으려면 dictionary를 사용하면 되지 않을까?
    # countedSubsets에서 set을 찾는 것 자체가 O(n)의 시간복잡도를 가지는 것도 문제네. 이것도 dictionary로 바꿔야겠네.

    # BackTrack의 순회 자체의 시간복잡도는 O(2^n)이다. => 감당 가능?
    # => backtrack이라서 시간복잡도는 O(2^n)이 아니다.
    def beautifulSubsets(self, nums: List[int], target_diff: int) -> int:
        def backTrack(nums: List[int], idx: int, num_cnt: defaultdict[int], target_diff: int) -> int:
            if idx == len(nums):
                # 주의: list내에서 set은 in으로 찾을 수 없다.
                if len(num_cnt) == 0:
                    return 0
                else:
                    return 1

            cnt = backTrack(nums, idx + 1, num_cnt, target_diff)

            current_num = nums[idx]
            if num_cnt[target_diff + current_num] == 0 and num_cnt[current_num - target_diff] == 0:
                num_cnt[current_num] += 1
                cnt += backTrack(nums, idx + 1, num_cnt, target_diff)
                num_cnt[current_num] -= 1
            return cnt
        
        return backTrack(nums, 0, defaultdict(int), target_diff)
    
    def countPairsWithDiff(self, nums: List[int], diff: int) -> int:
        num_counts = Counter(nums)

        def calculate_dp(num):
            if (num - diff) in num_counts:
                num_not_included_pair_count, num_included_pair_count = calculate_dp(num - diff)
            else:
                num_not_included_pair_count, num_included_pair_count = 1, 0
            return num_not_included_pair_count + num_included_pair_count, num_not_included_pair_count * (pow(2, num_counts[num]) - 1)

        total = 1
        for num in num_counts:
            if not num_counts[num + diff]:
                total *= sum(calculate_dp(num))
        return total - 1