# https://leetcode.com/problems/longer-contiguous-segments-of-ones-than-zeros/description/

class Solution:
    def checkZeroOnes(self, inputString: str) -> bool:
        lenLongestOne, lenLongestZero = 0, 0
        lenCurrentOne, lenCurrentZero = 0, 0

        for i in range(len(inputString)):
            if inputString[i] == '1':
                lenCurrentOne += 1
                lenCurrentZero = 0
            else:
                lenCurrentZero += 1
                lenCurrentOne = 0

            lenLongestOne = max(lenLongestOne, lenCurrentOne)
            lenLongestZero = max(lenLongestZero, lenCurrentZero)

        return lenLongestOne > lenLongestZero