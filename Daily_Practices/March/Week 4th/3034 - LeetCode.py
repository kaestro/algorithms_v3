# https://leetcode.com/problems/number-of-subarrays-that-match-a-pattern-i/description/

from typing import List

class Solution:
    # pattern의 size가 m일 때, 다음과 같은 조건을 만족하는 subarray의 개수를 반환하라.
    # 1. subarray의 size는 m + 1이다.
    # 2. subarray[k + 1] > subarray[k] if pattern[k] == 1
    # 3. subarray[k + 1] == subarray[k] if pattern[k] == 0
    # 4. subarray[k + 1] < subarray[k] if pattern[k] == -1

    # Brute Force Solution
    # nums[0] ~ nums[n - m]까지의 subarray를 모두 탐색하며, pattern과 일치하는 subarray의 개수를 세어 반환한다.
    # Time Complexity: O(n * m)
    def countMatchingSubarrays(self, nums: List[int], patterns: List[int]) -> int:

        result = 0

        for i in range(len(nums) - len(patterns)):
            for j in range(len(patterns)):
                if patterns[j] == 1 and nums[i + j + 1] <= nums[i + j]:
                    break
                elif patterns[j] == 0 and nums[i + j + 1] != nums[i + j]:
                    break
                elif patterns[j] == -1 and nums[i + j + 1] >= nums[i + j]:
                    break
            else:
                result += 1

        return result
    
    # nums의 각 원소 비교해서 pattern과 동일한 형태로 변환한 후, pattern의 size만큼씩 비교하며, 일치하는 subarray의 개수를 센다.
    # Time Complexity: O(n)
    def betterSolution(self, nums: List[int], pattern: List[int]) -> int:
        ans=[]
        for i in range(1, len(nums)):
            if(nums[i] == nums[i-1]):
                ans.append(0)
            elif(nums[i] > nums[i-1]):
                ans.append(1)
            else:
                ans.append(-1)
        
        k = len(pattern)
        result = 0

        for i in range(len(ans)):
            if(ans[i:i+k] == pattern):
                result += 1

        return result