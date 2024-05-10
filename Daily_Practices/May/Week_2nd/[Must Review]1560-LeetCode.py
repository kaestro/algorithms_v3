# https://leetcode.com/problems/most-visited-sector-in-a-circular-track/description/
from typing import List

class Solution:
    def mostVisited(self, n: int, rounds: List[int]) -> List[int]:
        rounds = [round - 1 for round in rounds]
        sectorVisits = [0] * n
        for i in range(len(rounds) - 1):
            start, end = rounds[i], rounds[i + 1]
            if start <= end:
                for j in range(start, end):
                    sectorVisits[j] += 1
            else:
                for j in range(start, n):
                    sectorVisits[j] += 1
                for j in range(0, end):
                    sectorVisits[j] += 1
        sectorVisits[rounds[-1]] += 1

        max_visits = max(sectorVisits)
        ans = [i + 1 for i, visits in enumerate(sectorVisits) if visits == max_visits]
        return ans
    
    # 결국 한바퀴를 돌면 방문한 횟수가 다 같다는 것을 알 수 있음
    # 이 때문에 처음과 끝만 보면 된다.
    def betterSolution(self, n: int, rounds: List[int]) -> List[int]:
        start, end = rounds[0], rounds[-1]
        if start <= end:
            return list(range(start, end + 1))
        else:
            return list(range(1, end + 1)) + list(range(start, n + 1))