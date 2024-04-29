# https://leetcode.com/problems/alternating-digit-sum/description/

class Solution:
    def alternateDigitSum(self, n: int) -> int:
        numStr = str(n)
        result, weight = 0, 1
        for i in range(len(numStr)):
            current_digit = int(numStr[i])
            result += current_digit * weight
            weight = -weight
        return result


if __name__ == "__main__":
    print(Solution().alternateDigitSum(10))