# https://leetcode.com/problems/reverse-only-letters/description/

class Solution:
    # Letters that are not English letters are not reversed
    def reverseOnlyLetters(self, s: str) -> str:

        reversed_letters = []
        not_reversed_letters_idxes = {}

        for idx, letter in enumerate(s):
            if letter.isalpha():
                reversed_letters.append(letter)
            else:
                not_reversed_letters_idxes[idx] = letter
        
        answer_list = []
        for i in range(len(s)):
            if i in not_reversed_letters_idxes:
                answer_list.append(not_reversed_letters_idxes[i])
            else:
                answer_list.append(reversed_letters.pop())

        return ''.join(answer_list)


    def reverseOnlyLetters(self, input_string: str) -> str:
        reversed_letters = ''
        for character in input_string:
            if character.isalpha():
                reversed_letters += character
        reversed_letters = reversed_letters[::-1]
        
        result, index = '', 0
        for character in input_string:
            if character.isalpha():
                result += reversed_letters[index]
                index += 1
            else:
                result += character
        return result