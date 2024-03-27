# https://leetcode.com/problems/split-with-minimum-sum/description/

class Solution:
    def splitNum(self, num: int) -> int:

        digits = []
        while num:
            digits.append(num % 10)
            num //= 10
        
        if len(digits) % 2 == 1:
            digits.append(0)

        digits.sort()

        left_num, right_num = 0, 0
        for i in range(0, len(digits), 2):
            left_num = left_num * 10 + digits[i]
            right_num = right_num * 10 + digits[i + 1]

        return left_num + right_num


if __name__ == "__main__":
    sample = Solution()

    print(sample.splitNum(4325))