# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/description/

class Solution:
    def countGoodSubstrings(self, input_string: str) -> int:
        count = 0
        for i in range(len(input_string) - 2):
            if len(set(input_string[i:i+3])) == 3:
                count += 1
        return count