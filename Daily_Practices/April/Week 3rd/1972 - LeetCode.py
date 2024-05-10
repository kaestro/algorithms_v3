# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/

class Solution:
    def minTimeToType(self, word: str) -> int:
        result = 0

        curr_char = 'a'
        char_to_num = {chr(i): i - 97 for i in range(97, 123)}

        for ch in word:
            result += min(abs(char_to_num[ch] - char_to_num[curr_char]), 26 - abs(char_to_num[ch] - char_to_num[curr_char])) + 1
            curr_char = ch

        return result