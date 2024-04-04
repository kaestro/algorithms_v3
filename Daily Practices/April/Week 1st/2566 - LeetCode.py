# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/description/

class Solution:
    def minMaxDifference(self, num: int) -> int:
        digits = [int(digit) for digit in str(num)]
        max_int, min_int = 0, 0

        min_int_to_change, max_int_to_change= -1, -1
        found_max_digit, found_min_digit = False, False
        for i, digit in enumerate(digits):
            if not found_max_digit:
                if digit != 9:
                    found_max_digit = True
                    max_int_to_change = digit
            
            if found_max_digit and digit == max_int_to_change:
                max_int = max_int * 10 + 9
            else:
                max_int = max_int * 10 + digit
            
            if not found_min_digit:
                if digit != 0:
                    found_min_digit = True
                    min_int_to_change = digit
            
            if found_min_digit and digit == min_int_to_change:
                min_int = min_int * 10
            else:
                min_int = min_int * 10 + digit
        
        return max_int - min_int