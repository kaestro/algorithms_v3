# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

from typing import List

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_idx_sum = float('inf')
        common_restaurants = []

        dict_str_idx = {list1[i]: i for i in range(len(list1))}

        for idx, restaurant in enumerate(list2):
            if restaurant in dict_str_idx:
                idx_sum = idx + dict_str_idx[restaurant]
                if idx_sum < min_idx_sum:
                    min_idx_sum = idx_sum
                    common_restaurants = [restaurant]
                elif idx_sum == min_idx_sum:
                    common_restaurants.append(restaurant)
        
        return common_restaurants