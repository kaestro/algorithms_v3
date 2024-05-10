# https://leetcode.com/problems/maximum-number-of-operations-with-the-same-score-i/description/

from typing import List
from collections import Counter

class Solution:
    def maxOperations(self, nums: List[int]) -> int:
        numsCounter, possibleSums = Counter(nums), self.getPossibleSums(nums)

        result = 0
        for possibleSum in possibleSums:
            numsOperations = self.getNumsOperations(possibleSum, numsCounter)
            result = max(result, numsOperations)

        return result

    def getPossibleSums(self, nums):
        possible_sums = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                possible_sums.add(nums[i] + nums[j])
        return possible_sums
    
    def getNumsOperations(self, possibleSum, numsCounter):
        numsCounter = numsCounter.copy()
        sortedNums = sorted(numsCounter.keys(), reverse=True)
        left, right = 0, len(sortedNums) - 1

        result = 0
        while left <= right:
            currentSum = sortedNums[left] + sortedNums[right]
            if currentSum < possibleSum:
                right -= 1
            elif currentSum > possibleSum:
                left += 1
            else:
                if left == right:
                    if numsCounter[sortedNums[left]] >= 2:
                        numsCounter[sortedNums[left]] -= 2
                        result += 1

                    if numsCounter[sortedNums[left]] <= 2:
                        break
                else:
                    if numsCounter[sortedNums[left]] > 0 and numsCounter[sortedNums[right]] > 0:
                        numsCounter[sortedNums[left]] -= 1
                        numsCounter[sortedNums[right]] -= 1
                        result += 1
                if numsCounter[sortedNums[left]] == 0:
                    left += 1
                if numsCounter[sortedNums[right]] == 0:
                    right -= 1

        return result

if __name__ == "__main__":
    sample = Solution()
    print(sample.maxOperations([3,2,6,1,4]))