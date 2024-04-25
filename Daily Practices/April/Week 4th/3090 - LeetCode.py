# https://leetcode.com/problems/maximum-length-substring-with-two-occurrences/description/

class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        left, right = 0, 0
        maxCount, charCounter = 1, {s[0]: 1}
        result = 0

        while right < len(s) - 1:
            right += 1
            self.incrementCount(s[right], charCounter)
            maxCount = max(maxCount, charCounter[s[right]])

            while (maxCount > 2):
                self.decrementCount(s[left], charCounter)
                left += 1
                maxCount = max(charCounter.values(), default=0)
            
            result = max(result, right - left + 1)
            
        return result

    def incrementCount(self, ch: str, charCounter: dict) -> None:
        charCounter[ch] = charCounter.get(ch, 0) + 1

    def decrementCount(self, ch: str, charCounter: dict) -> None:
        charCounter[ch] -= 1

if __name__ == "__main__":
    s = Solution()
    print(s.maximumLengthSubstring("bcbbbcba"))