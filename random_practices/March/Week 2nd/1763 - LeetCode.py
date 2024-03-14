# https://leetcode.com/problems/longest-nice-substring/description/

from collections import defaultdict

class Solution:
    # string is nice if both upper/lower case of each letter exists
    # brute force loop twice to create all substring
    # check if the substring is nice
    # when only incrementing the right pointer, using dictionary can help
    def longestNiceSubstring(self, input_string: str) -> str:

        longest_nice_substring = ""

        for i in range(len(input_string)):
            substring_dict = defaultdict(int)
            for j in range(i, len(input_string)):
                substring_dict[input_string[j]] += 1
                if self.is_nice(substring_dict) and len(input_string[i:j+1]) > len(longest_nice_substring):
                    longest_nice_substring = input_string[i:j+1]

        return longest_nice_substring
    
    def is_nice(self, substring_dict: defaultdict[int]):
        for key in substring_dict:
            if key.islower() and substring_dict[key.upper()] == 0:
                return False
            if key.isupper() and substring_dict[key.lower()] == 0:
                return False
        return True
    
    # Divide and Conquer
    # swapcase
    def bestSolution(self, s: str) -> str:
        char = set(s)
        for i, c in enumerate(s):
            if c.swapcase() not in char:
                return max(self.bestSolution(s[:i]), self.bestSolution(s[i+1:]), key = len)
        return s