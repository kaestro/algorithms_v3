# https://leetcode.com/problems/count-hills-and-valleys-in-an-array/description/

from typing import List

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        # Truncate the same numbers from the beginning
        while len(nums) > 1 and nums[0] == nums[1]:
            nums.pop(0)
        
        if len(nums) == 1:
            return 0

        hill_count = 0
        valley_count = 0
        is_Increasing = True if nums[0] < nums[1] else False

        for i in range(1, len(nums) - 1):
            if is_Increasing:
                if nums[i] > nums[i+1]:
                    is_Increasing = False
                    hill_count += 1
            else:
                if nums[i] < nums[i+1]:
                    is_Increasing = True
                    valley_count += 1

        return hill_count + valley_count
    
    def anotherSolution(self, nums: List[int]) -> int:
        count = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i + 1]: nums[i] = nums[i - 1]
            if (nums[i - 1] < nums[i] and nums[i + 1] < nums[i]) or (nums[i - 1] > nums[i] and nums[i + 1] > nums[i]): count += 1
        
        return count