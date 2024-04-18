# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/

from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[i].startswith(words[j]) and words[i].endswith(words[j]):
                    result += 1

        return result