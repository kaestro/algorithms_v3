# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/

from typing import List

class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        colorMinMaxIdx = {}
        for idx, color in enumerate(colors):
            if color not in colorMinMaxIdx:
                colorMinMaxIdx[color] = [idx, idx]
            else:
                colorMinMaxIdx[color][1] = idx
            
        maxDistance = -1

        for color in colorMinMaxIdx:
            minIdx, maxIdx = colorMinMaxIdx[color]
            for otherColor in colorMinMaxIdx:
                if color == otherColor:
                    continue
                otherMinIdx, otherMaxIdx = colorMinMaxIdx[otherColor]
                maxDistance = max(maxDistance, abs(minIdx - otherMaxIdx), abs(maxIdx - otherMinIdx))
        
        return maxDistance