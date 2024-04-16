# https://leetcode.com/problems/minimum-time-to-type-word-using-special-typewriter/description/

class Solution:
    def minTimeToType(self, word: str) -> int:
        result = 0

        curr_char = 'a'
        char_to_num = {chr(i): i - 97 for i in range(97, 123)}

        

        return result