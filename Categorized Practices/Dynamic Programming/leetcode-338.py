# https://leetcode.com/problems/counting-bits/description/

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:

        # Initialize the result array with zeros
        ans = [0] * (n+1) 

        for i in range(1, n+1):
            # Use the fact that the number of set bits in i is equal to
            # the nubmer of set bits in i // 2 + 1 if i is odd, or
            # the same as the number of set bits in i // 2 if i is even
            ans[i] = ans[i // 2] + (i % 2)

        return ans