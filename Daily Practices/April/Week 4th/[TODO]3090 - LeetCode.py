# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left, right = 0, 0
        maxCount, char_count = 1, {s[0]: 1}
        result = 0

        while right < len(s) - 1:
            right += 1
            self.incrementCount(s[right], char_count)
            maxCount = max(maxCount, char_count[s[right]])

            while (maxCount > 1) and not ((maxCount == 2) and self.onlyOneDuplicateTwo(char_count)):
                self.decrementCount(s[left], char_count)
                left += 1
                maxCount = max(char_count.values(), default=0)
            
            result = max(result, right - left + 1)
            
        return result

    def __init__(self):
        self.count_of_two = 0

    def incrementCount(self, char: str, char_count: dict) -> None:
        char_count[char] = char_count.get(char, 0) + 1
        if char_count[char] == 2:
            self.count_of_two += 1

    def decrementCount(self, char: str, char_count: dict) -> None:
        if char_count[char] == 2:
            self.count_of_two -= 1
        char_count[char] -= 1
        if char_count[char] == 0:
            del char_count[char]
    
    def onlyOneDuplicateTwo(self, char_count: dict) -> bool:
        return self.count_of_two == 1

if __name__ == "__main__":
    s = Solution()
    print(s.maximumLengthSubstring("bcbbbcba"))