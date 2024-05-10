# https://leetcode.com/problems/can-make-palindrome-from-substring/description/
# https://leetcode.com/problems/can-make-palindrome-from-substring/solutions/371999/python-100-runtime-and-memory/

from typing import List

class Solution:
    # query = [left, right, k]
    # [inputs_str[left:right+1]]에 대해 k번 이하로 문자를 임의의 lowercase English letter로 변경하여
    # 해당 substring이 palindrome이 되도록 할 수 있는지 여부를 반환하는 문제
    def canMakePaliQueries(self, input_str: str, queries: List[List[int]]) -> List[bool]:

        N = 26
        str_len = len(input_str)
        str_to_int = list(map(lambda x: ord(x) - ord('a'), input_str))

        dp = [0] * (str_len + 1)
        for i in range(1, str_len + 1):
            # dp[i]를 26bit의 binary로 표현한다. 각 bit는 해당 문자가 홀수번 등장했는지 짝수번 등장했는지를 나타낸다.
            dp[i] = dp[i - 1] ^ (1 << str_to_int[i - 1])
        
        # binary로 표현한 수의 1의 개수를 세는 함수
        ones_count = lambda x: bin(x).count('1')

        return [
            ones_count(dp[right + 1] ^ dp[left]) >> 1 <= k
            for left, right, k in queries
        ]


if __name__ == "__main__":
    sample = Solution()
    print(
        sample.canMakePaliQueries
        (
            "abcda",
            [[3,3,0],[1,2,0],[0,3,1],[0,3,2],[0,4,1]]
        )
    )