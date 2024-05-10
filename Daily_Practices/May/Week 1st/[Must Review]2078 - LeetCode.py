# https://leetcode.com/problems/two-furthest-houses-with-different-colors/description/

from typing import List

class Solution:
    def __init__(self):
        self.colorMinMaxIdx = {}
        self.minColor = None
        self.maxColor = None
        self.minIdx = float('inf')
        self.secondMinIdx = float('inf')
        self.maxIdx = float('-inf')
        self.secondMaxIdx = float('-inf')

    def setMin(self, color: int):
        if self.colorMinMaxIdx[color][0] < self.minIdx:
            if color != self.minColor:
                self.secondMinIdx = self.minIdx
            self.minIdx = self.colorMinMaxIdx[color][0]
            self.minColor = color
        elif self.colorMinMaxIdx[color][0] < self.secondMinIdx and color != self.minColor:
            self.secondMinIdx = self.colorMinMaxIdx[color][0]

    def setMax(self, color: int):
        if self.colorMinMaxIdx[color][1] > self.maxIdx:
            if color != self.maxColor:
                self.secondMaxIdx = self.maxIdx
            self.maxIdx = self.colorMinMaxIdx[color][1]
            self.maxColor = color
        elif self.colorMinMaxIdx[color][1] > self.secondMaxIdx and color != self.maxColor:
            self.secondMaxIdx = self.colorMinMaxIdx[color][1]


    def initialize(self, colors: List[int]):
        for idx, color in enumerate(colors):
            if color not in self.colorMinMaxIdx:
                self.colorMinMaxIdx[color] = [idx, idx]
            else:
                self.colorMinMaxIdx[color][1] = idx

            self.setMin(color)
            self.setMax(color)

    def calculateMaxDistance(self):
        maxDistance = -1

        for color in self.colorMinMaxIdx:
            colorMinIdx, colorMaxIdx = self.colorMinMaxIdx[color]
            if color != self.minColor:
                maxDistance = max(maxDistance, abs(self.minIdx - colorMaxIdx))
            else:
                maxDistance = max(maxDistance, abs(self.secondMinIdx - colorMaxIdx))
            
            if color != self.maxColor:
                maxDistance = max(maxDistance, abs(self.maxIdx - colorMinIdx))
            else:
                maxDistance = max(maxDistance, abs(self.secondMaxIdx - colorMinIdx))

        return maxDistance

    def maxDistance(self, colors: List[int]) -> int:
        self.initialize(colors)
        return self.calculateMaxDistance()

if __name__ == "__main__":
    print(Solution().maxDistance([1,1,1,6,1,1,1]))