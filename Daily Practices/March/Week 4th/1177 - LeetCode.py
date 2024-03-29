# https://leetcode.com/problems/can-make-palindrome-from-substring/description/

from typing import List

class Solution:
    # query = [left, right, k]
    # [inputs_str[left:right+1]]에 대해 k번 이하로 문자를 임의의 lowercase English letter로 변경하여
    # 해당 substring이 palindrome이 되도록 할 수 있는지 여부를 반환하는 문제

    # rearrange에 대해 생각하지 못함
    def canMakePaliQueries(self, input_str: str, queries: List[List[int]]) -> List[bool]:

        result = []

        def not_palindrome_count(substr: str) -> int:
            count = 0
            for i in range(len(substr)//2):
                if substr[i] != substr[len(substr)-1-i]:
                    count += 1
            return count

        for query in queries:
            left, right, k = query
            substr = input_str[left:right+1]
            if not_palindrome_count(substr) <= k:
                result.append(True)
            else:
                result.append(False)

        return result