# https://leetcode.com/problems/smallest-missing-integer-greater-than-sequential-prefix-sum/description/

from typing import List

class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        prefix_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1] + 1:
                prefix_sum += nums[i]
            else:
                break
        
        sorted_set = sorted(set(nums))
        if prefix_sum not in sorted_set:
            return prefix_sum

        idx = sorted_set.index(prefix_sum)
        if idx == len(sorted_set) - 1:
            return prefix_sum + 1

        for i in range(idx + 1, len(sorted_set)):
            prefix_sum += 1
            if sorted_set[i] != prefix_sum:
                return prefix_sum

        return prefix_sum + 1

if __name__ == "__main__":
    print(Solution().missingInteger([3,4,7,6,6,5,8,2,8,9,2,6]))