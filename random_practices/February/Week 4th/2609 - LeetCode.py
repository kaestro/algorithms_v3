# https://leetcode.com/problems/find-the-longest-balanced-substring-of-a-binary-string/description/

class Solution:
    # balanced string is a string that has an equal number of 0s and 1s
    # where 0s are in the left and 1s are in the right
    # find the longest balanced substring
    def findTheLongestBalancedSubstring(self, binaryString: str) -> int:
        isZero, zeroCnt, oneCnt = False, 0, 0

        maxLen = 0

        for char in binaryString:
            if char == '0':
                if not isZero:
                    isZero, zeroCnt, oneCnt = True, 1, 0
                else:
                    zeroCnt += 1
            else:
                if isZero:
                    isZero = False
                oneCnt += 1
                if oneCnt <= zeroCnt:
                    maxLen = max(maxLen, 2 * oneCnt)

        return maxLen