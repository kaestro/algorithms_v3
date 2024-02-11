# https://leetcode.com/problems/word-subsets/description/

from typing import List
from collections import Counter

# 1. 특정 string이 string list의 모든 element를 subset으로 가지고 있는지 확인한다.
# 2. 그러한 string을 모두 찾아서 return한다.

# Question1. string이 다른 string을 subset으로 가지는 지 확인할 방법은?
# Questions2. 해당 방법으로 꼭 모든 string을 검색해야만 하는가? => 검증 방식이 너무 크면, 다른 방법 취함.

class Solution:
    def wordSubsets(self, potential_universal_strings: List[str], subset_strings: List[str]) -> List[str]:
        max_char_counter = Counter()
        for string in subset_strings:
            max_char_counter |= Counter(string)

        return [string for string in potential_universal_strings if self.is_subset_by_counter(string, max_char_counter)]


    # check whether the potential_subset is subset of main_word
    # Solution 1. Using Counter
    # Counter의 경우, O(n)으로 동작한다.
    # key, value를 모두 순회 하는 것은 O(n)이다.
    # 따라서 time complexity는 O(n)이다.
    # 이 방법을 쓰면, words2의 counter를 쓸데없이 매번 돌아야됨.
    def is_subset(self, main_word: str, potential_subset: str) -> bool:
        main_counter = Counter(main_word)
        potential_counter = Counter(potential_subset)
        for key, value in potential_counter.items():
            if main_counter[key] < value:
                return False
        return True

    def is_subset_by_counter(self, main_word: str, potential_subset_counter: Counter) -> bool:
        main_counter = Counter(main_word)
        for key, value in potential_subset_counter.items():
            if main_counter[key] < value:
                return False
        return True