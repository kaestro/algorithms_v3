# https://leetcode.com/problems/self-dividing-numbers/description/

from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def digits_set(n):
            return set(int(digit) for digit in str(n))
        
        ans = []

        for num in range(left, right + 1):
            digits = digits_set(num)
            if 0 in digits or any(num % digit != 0 for digit in digits):
                continue
            ans += [num]

        return ans