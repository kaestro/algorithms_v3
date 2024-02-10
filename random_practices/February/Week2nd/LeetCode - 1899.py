# https://leetcode.com/problems/merge-triplets-to-form-target-triplet/description/

from typing import List

# 각각의 triplet들에 대해 세 값이 모두 target의 값보다 작거나 같은지 확인한다.
# 하나라도 크다면 해당 triplet은 target triplet을 만들 수 없다.
# 작거나 같을 경우 merge 함수를 통해 현재 triplet과 합치고, target triplet과 같은지 확인한다.
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        current_triplet = [0, 0, 0]

        for triplet in triplets:
            if all(element <= target[i] for i, element in enumerate(triplet)):
                current_triplet = self.merge(current_triplet, triplet)
                if current_triplet == target:
                    return True

        return False
    
    def merge(self, left_triplet: List[int], right_triplet: List[int]) -> List[int]:
        return [max(left_triplet[0], right_triplet[0]), max(left_triplet[1], right_triplet[1]), max(left_triplet[2], right_triplet[2])]
        