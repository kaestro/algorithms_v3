# https://leetcode.com/problems/lemonade-change/description/

from typing import List

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        balance = {5: 0, 10: 0, 20: 0}
        for bill in bills:
            balance[bill] += 1
            if bill == 10:
                balance[5] -= 1
                if balance[5] < 0:
                    return False
            elif bill == 20:
                if balance[10] > 0:
                    balance[10] -= 1
                    balance[5] -= 1
                else:
                    balance[5] -= 3
                if balance[5] < 0:
                    return False
        return True