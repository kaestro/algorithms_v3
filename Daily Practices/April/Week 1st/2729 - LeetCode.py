# https://leetcode.com/problems/check-if-the-number-is-fascinating/description/

class Solution:
    def isFascinating(self, n: int) -> bool:
        concat_num = str(n) + str(n * 2) + str(n * 3)
        bitsum = 0

        for digit in concat_num:
            bitsum += 1 << int(digit)

        return bitsum == bin(2**9 - 1) * 2