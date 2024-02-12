# https://leetcode.com/problems/fair-candy-swap/description/
from typing import List

class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        ans = [-1, -1]
        diff = (sum(aliceSizes) - sum(bobSizes))

        diff //= 2

        for alice in aliceSizes:
            if alice - diff in bobSizes:
                ans = [alice, alice - diff]
                break
        
        return ans
    
    # Python의 Set은 Hash Table로 구현되어 있어서, in 연산의 시간복잡도가 O(1)이다.
    # 이 때문에 위의 코드의 O(N*M)에서 O(N+M)으로 줄일 수 있다.
    def betterCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        aliceSizes = set(aliceSizes)
        for bob in bobSizes:
            if bob + diff in aliceSizes:
                return [bob + diff, bob]
        return []