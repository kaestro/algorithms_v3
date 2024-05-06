# https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/description/
from typing import List

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        powers = [sum(row) for row in mat]
        sorted_powers = sorted([(power, i) for i, power in enumerate(powers)])
        return [index for _, index in sorted_powers[:k]]

if __name__ == "__main__":
    print(Solution().kWeakestRows([[1,1,0,0,0],
                                    [1,1,1,1,0],
                                    [1,0,0,0,0]], 2))