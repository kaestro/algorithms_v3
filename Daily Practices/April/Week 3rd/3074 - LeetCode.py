# https://leetcode.com/problems/apple-redistribution-into-boxes/

from typing import List
from heapq import heapify, heappop

class Solution:
    def minimumBoxes(self, apples: List[int], capacities: List[int]) -> int:
        result = 0

        max_heap = [-capacity for capacity in capacities]
        heapify(max_heap)
        
        remnant = 0
        for apple in apples:
            while apple > 0:
                if apple > remnant:
                    apple -= remnant
                    remnant = -heappop(max_heap)
                    result += 1
                else:
                    remnant -= apple
                    apple = 0

        return result