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

        result = []

        char_count_until_i = [Counter()]
        for i in range(1, len(input_str) + 1):
            char_count_until_i.append(char_count_until_i[i - 1] + Counter(input_str[i - 1]))

        def not_palindrome_count(char_counter) -> int:
            result = 0
            for count in char_counter.values():
                if count % 2 != 0:
                    result += 1
            result //= 2
            return result
        
        for query in queries:
            left, right, k = query
            char_counter = char_count_until_i[right + 1] - char_count_until_i[left]
            needed_change_count = sum(v % 2 for v in char_counter.values()) // 2
            result.append(not_palindrome_count(char_counter) <= k)

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