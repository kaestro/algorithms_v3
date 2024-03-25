# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/description/

from typing import List
from collections import Counter


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        maxInt = max(arr)
        countInt = Counter(arr)
        
        minCnt = 1
        while k >= minCnt:
            for number, cnt in countInt.items():
                if cnt == minCnt:
                    countInt[number] = 0
                    k -= minCnt
                if k < minCnt:
                    break
            minCnt += 1

        # must be changed for this is not the answer
        return sum(1 for cnt in countInt.values() if cnt != 0)

if __name__ == "__main__":
    arr = [1,1,2,2,3,3]
    k = 3

    print(Solution().findLeastNumOfUniqueInts(arr, k))