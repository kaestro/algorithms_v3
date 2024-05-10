# https://leetcode.com/problems/check-if-the-number-is-fascinating/description/

class Solution:
    def isFascinating(self, n: int) -> bool:
        concat_num = str(n) + str(n * 2) + str(n * 3)
        bitsum, ord_zero = 0, ord('0')

        for digit in concat_num:
            bitsum += 1 << ord(digit) - ord_zero

        return bitsum == 2 ** 10 - 2