# https://leetcode.com/problems/intersection-of-multiple-arrays/description/

from typing import List

class Solution:
    # nums_list는 distinct positive integers로 이루어진 2차원 리스트이다.
    # 각각의 리스트 별로 오름차순 정렬된 subset들이 있다고 할 때,
    # 이들의 교집합을 반환하라.
    def intersection(self, nums_list: List[List[int]]) -> List[int]:

        # O(n^2) solution => 결과적으로는 최소 O(k*n^2)를 야기하므로 최적의 해결책은 아니다.
        # input_size가 최대 1000으로 주어져있기 때문에 O(n^3)이라고 볼 수도 있음.
        def findAscendingSubsets(nums: List[int]) -> List[List[int]]:
            subsets = []
            subset = []
            for i in range(len(nums)):
                if i == 0 or nums[i] > nums[i - 1]:
                    subset.append(nums[i])
                
                subsets.append(subset)

            return subsets

        return [-1]