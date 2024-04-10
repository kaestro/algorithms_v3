# https://leetcode.com/problems/find-score-of-an-array-after-marking-all-elements/description/

from typing import List
from heapq import heappop, heapify

# 1. choose smallest element
# 2. if there are multiple smallest elements, choose the one with the smallest index
# 3. add the smallest element to the score
# 4. mark the element and its neighbors as visited
class Solution:
    # Brute Force
    # Use a heap to find the smallest element
    # Then remove the element and its neighbors from the heap

    # Bottle Neck
    # 1. heapify is O(n)
    # 2. remove is O(n)
    
    # Question: Do I need to remove the element from heap_nums?
    def findScore(self, nums: List[int]) -> int:
        result = 0

        heap_nums = [(num, idx) for idx, num in enumerate(nums)]
        heapify(heap_nums)

        while heap_nums:
            num, idx = heappop(heap_nums)

            result += num

            if idx > 0 and (nums[idx - 1], idx - 1) in heap_nums:
                heap_nums.remove((nums[idx - 1], idx - 1))
            
            if idx < len(nums) - 1 and (nums[idx + 1], idx + 1) in heap_nums:
                heap_nums.remove((nums[idx + 1], idx + 1))
            
            heapify(heap_nums)

        return result

# Test
if __name__ == "__main__":
    sample = Solution()
    print(sample.findScore([10,44,10,8,48,30,17,38,41,27,16,33,45,45,34,30,22,3,42,42]))