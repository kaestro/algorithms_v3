# https://leetcode.com/problems/longest-nice-substring/description/

class Solution:
    # string is nice if both upper/lower case of each letter exists
    # brute force loop twice to create all substring
    # check if the substring is nice
    # when only incrementing the right pointer, using dictionary can help
    def longestNiceSubstring(self, s: str) -> str:
        opposite_exists = {}

        for letter in s:
            if (letter.lower() and letter.upper()) not in opposite_exists:
                opposite_exists[letter] = False
            elif letter not in opposite_exists:
                if letter.islower():
                    opposite_exists[letter.upper()] = True
                else:
                    opposite_exists[letter.lower()] = True

        return "False"