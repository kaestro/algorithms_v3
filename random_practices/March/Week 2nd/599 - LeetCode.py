# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        dict_str_idx_sum = {word: idx for idx, word in enumerate(list1)}
        visited_str = set()

        for idx, word in enumerate(list2):
            if word in dict_str_idx_sum:
                dict_str_idx_sum[word] += idx
                visited_str.add(word)
        
        dict_str_idx_sum = {k: v for k, v in dict_str_idx_sum.items() if k in visited_str}
        min_idx_sum = min(dict_str_idx_sum.values())

        return [k for k, v in dict_str_idx_sum.items() if v == min_idx_sum]