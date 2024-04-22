# https://leetcode.com/problems/count-prefix-and-suffix-pairs-i/description/

from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        result = 0
        for i in range(len(words)):
            for j in range(i + 1, len(words)):
                if words[j].startswith(words[i]) and words[j].endswith(words[i]):
                    result += 1

        return result