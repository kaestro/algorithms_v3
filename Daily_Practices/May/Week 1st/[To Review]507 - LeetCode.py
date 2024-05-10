# https://leetcode.com/problems/perfect-number/description/

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False

        def get_factors(num):
            factors = []
            for i in range(1, int(num ** 0.5) + 1):
                if num % i == 0:
                    factors.append(i)
                    factors.append(num // i)
            return factors
        
        factors = get_factors(num)
        factors_sum = sum(factors)

        return factors_sum - num == num