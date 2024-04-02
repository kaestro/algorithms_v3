# https://leetcode.com/problems/maximum-repeating-substring/description/

class Solution:
    # sequence에서 word가 연속적으로 반복되는 최대 횟수를 반환
    def maxRepeating(self, sequence: str, word: str) -> int:

        word_len = len(word)
        idx = 0
        result = 0
        word_len = len(word)

        while idx < len(sequence):
            if sequence[idx] != word[0]:
                idx += 1
                continue
        
            current_count = 0
            while sequence[idx:idx + word_len] == word:
                idx += word_len
                current_count += 1
            else:
                idx += 1
                result = max(result, current_count)

        return result