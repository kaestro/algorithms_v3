# https://leetcode.com/explore/learn/card/sorting/694/comparison-based-sorts/4484/
# Implementation of Bubble Sort

from typing import List

class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        has_Changed = True
        expected = heights.copy()

        while has_Changed:
            has_Changed = False
            for i in range(len(expected)-1):
                if expected[i] > expected[i+1]:
                    expected[i], expected[i+1] = expected[i+1], expected[i]
                    has_Changed = True

            if not has_Changed:
                break
        
        cnt_diffs = sum(height != exp for height, exp in zip(heights, expected))
        
        return cnt_diffs



if __name__ == "__main__":
    sample = Solution()
    heights = [5,1,2,3,4]
    print(sample.heightChecker(heights))