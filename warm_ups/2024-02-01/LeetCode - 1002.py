# https://leetcode.com/problems/find-common-characters/description/

from typing import List
from collections import Counter

class Solution:

    def count_chars(self, s):
        cnt = Counter(s)
        for char in map(chr, range(ord('a'), ord('z')+1)):
            if char not in cnt:
                cnt[char] = 0
        return cnt

    def commonChars(self, words: List[str]) -> List[str]:
        count_list = [self.count_chars(word) for word in words]
        maxCount = {char: min(count[char] for count in count_list if char in count)
                    for char in map(chr, range(ord('a'), ord('z')+1))}
        return [char for char in maxCount for _ in range(maxCount[char])]
    
    def betterSolution(self, words: List[str]) -> List[str]:
        result = Counter(words[0])
        for word in words[1:]:
            result &= Counter(word)
        return list(result.elements())
    
    def bestSolution(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words
        res = []
        word1 = set(words[0])
        for char in word1:
            frequency = min([word.count(char) for word in words])
            res += [char] * frequency
        return res