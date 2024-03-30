# https://leetcode.com/problems/can-make-palindrome-from-substring/description/

from typing import List
from collections import defaultdict
from collections import Counter

class Solution:
    # query = [left, right, k]
    # [inputs_str[left:right+1]]에 대해 k번 이하로 문자를 임의의 lowercase English letter로 변경하여
    # 해당 substring이 palindrome이 되도록 할 수 있는지 여부를 반환하는 문제

    # rearrange에 대해 생각하지 못함
    def canMakePaliQueries(self, input_str: str, queries: List[List[int]]) -> List[bool]:

        N = 26
        a_int = ord('a')
        dp = [[0] * N]
        for i in range(1, len(input_str) + 1):
            dp.append(dp[i-1][:])
            dp[i][ord(input_str[i-1]) - a_int] ^= 1

        result = []
        for left, right, k in queries:
            result.append(sum((dp[right+1][i] ^ dp[left][i]) for i in range(N) ) // 2 <= k)

        return result


if __name__ == "__main__":
    sample = Solution()
    print(
        sample.canMakePaliQueries
        (
            "abcda",
            [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
        )
    )