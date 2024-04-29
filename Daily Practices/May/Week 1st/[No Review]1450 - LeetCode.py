# https://leetcode.com/problems/number-of-students-doing-homework-at-a-given-time/description/

from typing import List

class Solution:
    def busyStudent(self, startTime: List[int], endTime: List[int], queryTime: int) -> int:
        numStudent = 0
        for i in range(len(startTime)):
            if startTime[i] <= queryTime <= endTime[i]:
                numStudent += 1
        return numStudent