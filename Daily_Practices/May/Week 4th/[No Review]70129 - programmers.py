# https://school.programmers.co.kr/learn/courses/30/lessons/70129
from typing import List


def solution(binary_string: str) -> List[int]:

    removed_zero_cnt, repitition_cnt = 0, 0
    while binary_string != "1":
        original_length = len(binary_string)
        binary_string = remove_zero(binary_string)
        removed_zero_cnt += original_length - len(binary_string)

        binary_string = string_length_to_binary(binary_string)
        repitition_cnt += 1

    return [repitition_cnt, removed_zero_cnt]


def remove_zero(binary_string: str) -> str:
    return binary_string.replace("0", "")


def string_length_to_binary(binary_string: str) -> int:
    return bin(len(binary_string)).replace("0b", "")


if __name__ == "__main__":
    print(solution("110010101001"))  # [3, 8]
    print(solution("01110"))  # [3, 3]
    print(solution("1111111"))  # [4, 1]
    print(solution("1111110"))  # [2, 1]
    print(solution("111110"))  # [3, 2]
    print(solution("1111000"))  # [3, 3]
    print(solution("1111001"))  # [3, 2]
    print(solution("1111010"))  # [3, 3]
    print(solution("1111011"))  # [3, 2]
    print(solution("1111100"))  # [3, 2]
    print(solution("1111101"))  # [3, 1]
    print(solution("1111110"))  # [2, 1]
    print(solution("1111111"))  # [4, 1]
    print(solution("11111110"))  # [2, 1]
    print(solution("11111111"))  # [8, 1]
    print(solution("111111110"))  # [2, 1]
    print(solution("111111111"))  # [9, 1]
    print(solution("1111111110"))  # [2, 1]
    print(solution("1111111111"))  # [10, 1]
    print(solution("11111111110"))  # [2, 1]
    print(solution("11111111111"))  # [11, 1]
    print(solution("111111111110"))  # [2, 1]
    print(solution("111111111111"))  # [12, 1]
    print(solution("1111111111110"))  # [2, 1]
    print(solution("1111111111111"))  # [13, 1]
    print(solution("11111111111110"))  # [2, 1]
    print(solution("11111111111111"))  # [14, 1]
    print(solution("111111111111110"))  # [2, 1]
    print(solution("111111111111111"))  # [15, 1]
    print(solution("1111111111111110"))  # [2, 1]
